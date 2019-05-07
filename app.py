#!flask/bin/python


"""
@BuradaVivek
@vivekburada97@gmail.com
@This project is built for UpGrad
"""

import os
from flask import Flask, jsonify,abort,session,render_template
import time
import hashlib
import re
from flask import make_response
import datetime
from flask_cors import CORS,cross_origin
import random
import sqlite3 as sql
from flask_mail import Mail, Message
from flask_login import LoginManager, current_user, login_user, logout_user, login_required, UserMixin


'''
@BuradaVivek
@database initials
'''
# @BuradaVivek Test if DATA TABLE exits and populate if not
search = sql.connect('data.db')
search_table ="SELECT name FROM sqlite_master WHERE type='table' AND name='DATA';"
cursor = search.execute(search_table)
result = cursor.fetchone()

if result == None:
        print ("-----------------DATABASE CREATION  : DATA-----------------")
        search.execute('''CREATE TABLE DATA
                 (
                 ID  INT  PRIMARY KEY   NOT NULL,
                 DUMP   TEXT   collate nocase  NOT NULL);
                 ''')
        print ("Table created successfully")

        try:
            search.execute(''' INSERT INTO DATA (ID,DUMP)
                VALUES (1, 'LOUIS CARON Stylish 15.6 waterproof laptop Backpack 25 L Backpack  (Red, Purple) Men  Women 15.6 17 18, 19 25 L 25L  Polyester');''');
            print("---------",1,"---------------")
            search.execute(''' INSERT INTO DATA (ID,DUMP)
             VALUES (2, 'American Tourister Fizz Sch Bag 32 L Backpack  (Black, Grey) 32L Men  Women');''');
            print("---------",2,"---------------",)
            search.execute(''' INSERT INTO DATA (ID,DUMP)
              VALUES (3, 'Skybags Brat 4 Backpack  (Blue)
                    Front Stash Pocket, Mesh Bottle Holder at Side, Padded Handles, Dual Straps Fabric Lightweight');''');
            print("---------",3,"---------------")
            search.execute(''' INSERT INTO DATA (ID,DUMP)
             VALUES (4, 'ADIDAS LIN PER BP 15 L Backpack  (Blue) MYSINK / WHITE / WHITE 15L 15 L ');''');
            print("---------",4,"---------------")
            search.execute(''' INSERT INTO DATA (ID,DUMP)
              VALUES (5, 'Wildcraft Stanza 23 L Backpack   (Grey)  Solid 23L Men  Women');''');
            print("---------",5,"---------------")
            search.execute(''' INSERT INTO DATA (ID,DUMP)
              VALUES (6, 'Billion HiStorage 30 L Backpack  (Black)  30L Black Men  Women');''');
            print("---------",6,"---------------")
            search.commit()
            print("TOTAL INSERTED SUCCESSFULLY",search.total_changes,"--------------")

        except (sqlite.OperationalError, msg):
            print("Error")
        query = "SELECT * FROM DATA;"
        cursor = search.execute(query)
        result = cursor.fetchall()
        for row in result:
                 print("INSERTED--------------",row[0],"=========>",row[1])
else:
        print ("-----------------DATABASE PRESENT :  DATA-----------------")
search.close()



# @BuradaVivek Test if USER TABLE exits and populate if not
user = sql.connect('user.db')
user_table ="SELECT name FROM sqlite_master WHERE type='table' AND name='USER';"
cursor = user.execute(user_table)
result = cursor.fetchone()
if result == None:
        print ("-----------------DATABASE CREATION: USER-----------------")
        user.execute('''CREATE TABLE USER
                 (
                 USERNAME  TEXT  PRIMARY KEY   NOT NULL,
                 PASSWORD   TEXT     NOT NULL);
                 ''')

        print ("Table created successfully")


else:
        print ("-----------------DATABASE PRESENT: USER-----------------")
user.close()






app = Flask(__name__, template_folder='templates')
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = ''
app.config['SECRET_KEY'] = "lkkajdghdadkglajkgam"


@login_manager.user_loader
def load_user(user_id):
    return User(user_id)

class User(UserMixin):
  def __init__(self,id):
    self.id = id



CORS(app)
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)



# @BuradaVivek Mail Configurations
mail=Mail(app)
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'rewardnxt@gmail.com'
app.config['MAIL_PASSWORD'] = 'ababbaba@999'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)



# @BuradaVivek Mail the Session Holder

@app.route('/api/v1/wishlist', methods=['POST'])
def list_cat():
    if not request.json :
        abort(400)
    data = request.json
    list=[]
    list.append(data["user"])
    print("---------MAIL MAN  : ",list,"---------------")
    msg = Message('Wishlist product', sender = 'rewardnxt@gmail.com', recipients = list)
    msg.body = "You have a Product : "+ data["name"] +"  of Quantity  "+data["quantity"] + "  Buy now at Total  : "+data["total"]+".   Clear Your Wishlist today!"
    mail.send(msg)
    print("------------MAILED SUCCESSFULLY --------------------")
    return make_response(jsonify(),200)

def register_user(data):
    print(data)
    with sql.connect("user.db") as conn:
        query = " INSERT INTO USER (USERNAME,PASSWORD) VALUES ('"+data["username"]+"','"+data["pass"]+"')"
        print(query)
        conn.execute(query)
        conn.commit()
        print("---------------------USER ADDED------------------")

# @BuradaVivek Run Backend  http://127.0.0.1:5000/
@app.route('/')
def hello_world():
    return render_template('index.html')



# @BuradaVivek Resolve Search here
from flask import request

@app.route('/api/v1/search/<search>',methods=['GET'])
def search(search):

     with sql.connect("data.db") as conn:
        cursor = conn.execute("select * from DATA where DUMP like ? order by RANDOM()",
            ('%'+search+'%',))
        result = cursor.fetchone()
        if result == None:
            print('----------No DATA-------------')
            jsonify({"i":0}), 400
        else:
                print(result[0],"------",result[1])
                return jsonify({"i":result[0]}), 200

     return jsonify({"i":0}), 400

# @BuradaVivek Login User
@app.route('/api/v1/users/login', methods=['POST'])
def login():
    if not request.json or not 'name' in request.json:
        abort(400)
    flag=0
    data={'username':request.json['name'],
        'pass':request.json['pass']
        }
    with sql.connect("user.db") as conn:
        query = "SELECT USERNAME, PASSWORD from USER where USERNAME ='"+data["username"]+"'  AND PASSWORD ='" +data['pass']+"';"
        cursor = conn.execute(query)
        result = cursor.fetchone()
    if result == None:
        print("------------USER NOT EXIST --------------------")
        flag = 0
    else:
        print("---------------USER EXISTS ---------------------")
        flag = 1
    if(flag==1):
        user = User(data['username'])
        login_user(user)
        print(user.id)
        return make_response(jsonify(),200)
    else:
        return make_response(jsonify(),400)

#
#
# #@BuradaVivek Login User
# @app.route('/')
# def landing():
#     print(session['username'])
#     return render_template('index.html')
#


# @BuradaVivek Register User
@app.route('/api/v1/users/register', methods=['POST'])
def add_user():
    if not request.json or not 'name' in request.json:
        abort(400)
    data={'username':request.json['name'],
        'pass':request.json['pass']
        }
    with sql.connect("user.db") as conn:
        query = "SELECT USERNAME from USER where USERNAME ='"+data["username"]+"';"
        cursor = conn.execute(query)
        result = cursor.fetchone()
    if result == None:
        print("------------USER NOT EXIST --------------------")
        flag = 0
    else:
        print("---------------USER EXISTS ---------------------")
        flag = 1

    if(flag==0):
        print("---------------------ADDING USER---------------------")
        register_user(data)
        return jsonify({}),201
    else:
        return jsonify(),400


@app.route('/landing.html')
def index():
    print("----BAD-----",current_user.get_id())
    return render_template('landing.html',user = current_user.get_id())



@app.route('/api/v1/users/logout',methods=['GET'])
@login_required
def logout():
    logout_user()
    return make_response(jsonify(),200)




if __name__ == '__main__':
    app.run(debug=True)
