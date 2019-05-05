#!flask/bin/python


"""
@BuradaVivek
@vivekburada97@gmail.com
@This project is built for UpGrad
"""


from flask import Flask, jsonify,abort,session
import time
import hashlib
import re
from flask import make_response
import datetime
from flask_cors import CORS,cross_origin
import random
import sqlite3 as sql
from flask_mail import Mail, Message

'''
@BuradaVivek
@database initials
'''

user = sql.connect('user.db')
search = sql.connect('data.db')

# @BuradaVivek Test if DATA TABLE exits and populate if not
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
        search.execute(''' INSERT INTO DATA (ID,DUMP)
            VALUES (1, 'LOUIS CARON Stylish 15.6 waterproof laptop Backpack 25 L Backpack  (Red, Purple) Men  Women 15.6 17 18, 19 25 L 25L  Polyester');''');
        search.execute(''' INSERT INTO DATA (ID,DUMP)
         VALUES (2, 'American Tourister Fizz Sch Bag 32 L Backpack  (Black, Grey) 32L Men  Women');''');
        search.execute(''' INSERT INTO DATA (ID,DUMP)
          VALUES (3, 'Skybags Brat 4 Backpack  (Blue)
                Front Stash Pocket, Mesh Bottle Holder at Side, Padded Handles, Dual Straps Fabric Lightweight');''');
        search.execute(''' INSERT INTO DATA (ID,DUMP)
         VALUES (4, 'ADIDAS LIN PER BP 15 L Backpack  (Blue) MYSINK / WHITE / WHITE 15L 15 L ');''');
        search.execute(''' INSERT INTO DATA (ID,DUMP)
          VALUES (5, 'Wildcraft Stanza 23 L Backpack   (Grey)  Solid 23L Men  Women');''');
        search.execute(''' INSERT INTO DATA (ID,DUMP)
          VALUES (6, 'Billion HiStorage 30 L Backpack  (Black)  30L Black Men  Women');''');

        print ("Table created successfully")

else:
        print ("-----------------DATABASE PRESENT :  DATA-----------------")



# @BuradaVivek Test if USER TABLE exits and populate if not
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



'''
@BuradaVivek
@This is flask mail Component

'''


app = Flask(__name__)
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
    return session['username']


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
    text = "Hello"
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
        session['username'] = data["username"]
        print(session['username'])
        print("---------------USER EXISTS ---------------------")
        flag = 1

    if(flag==1):
        return make_response(jsonify(),200)
    else:
        return make_response(jsonify(),400)



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
        print("adding")
        register_user(data)
        return jsonify({}),201
    else:
        return jsonify(),400

#
# @app.route('/api/v1/users/logout',methods=['GET'])
# def logout():
#     if(session.pop('username', None)):
#         return make_response(jsonify(),200)
#     else:
#         return make_response(jsonify(),400)
#


if __name__ == '__main__':
    app.secret_key = 'super secret key'
    app.run(debug=True)
