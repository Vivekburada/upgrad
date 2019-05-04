"""
@BuradaVivek
@vivekburada97@gmail.com
@This project is built for UpGrad
"""
from flask import Flask , Blueprint , url_for

import sqlite3 as sql

conn = sql.connect('data.db')
print ("Opened database successfully")

sql_table ="SELECT name FROM sqlite_master WHERE type='table' AND name='DATA';"


cursor = conn.execute(sql_table)
result = cursor.fetchone()
if result == None:
        print("FALSE")
        conn.execute('''CREATE TABLE DATA
                 (
                 ID  INT  PRIMARY KEY   NOT NULL,
                 DUMP   TEXT   collate nocase  NOT NULL);
                 ''')
        conn.execute(''' INSERT INTO DATA (ID,DUMP)
            VALUES (1, 'LOUIS CARON Stylish 15.6 waterproof laptop Backpack 25 L Backpack  (Red, Purple) Men  Women 15.6 17 18, 19 25 L 25L  Polyester');''');

        conn.execute(''' INSERT INTO DATA (ID,DUMP)
         VALUES (2, 'American Tourister Fizz Sch Bag 32 L Backpack  (Black, Grey) 32L Men  Women');''');
        conn.execute(''' INSERT INTO DATA (ID,DUMP)
          VALUES (3, 'Skybags  Skybag Brat 4 Backpack  (Blue)
                Front Stash Pocket, Mesh Bottle Holder at Side, Padded Handles, Dual Straps Fabric Lightweight');''');
        conn.execute(''' INSERT INTO DATA (ID,DUMP)
         VALUES (4, 'ADIDAS LIN PER BP 15 L Backpack  (Blue) MYSINK / WHITE / WHITE 15L 15 L ');''');
        conn.execute(''' INSERT INTO DATA (ID,DUMP)
          VALUES (5, 'Wildcraft Stanza 23 L Backpack   (Grey)  Solid 23L Men  Women');''');
        conn.execute(''' INSERT INTO DATA (ID,DUMP)
          VALUES (6, 'Billion HiStorage 30 L Backpack  (Black)  30L Black Men  Women');''');




        conn.commit();

        print ("Table created successfully")


else:
        print ("TRUE")






# conn.execute('''DROP TABLE COMPANY''')

# conn.close()

app = Flask(__name__)

@app.route("/")
def index():
    flag = 'skybags'
    with sql.connect("data.db") as conn:
        cursor = conn.execute("select * from DATA where DUMP like ?",
            ('%'+flag+'%',))
        if cursor == None:
            print('----------No DATA-------------')
            return "NO DATA"
        else:
            for row in cursor:
                print(row[0],"------",row[1])
                return "DATA"
        return "SHIT HAPPENED"








"""
@BuradaVivek
/route/<Parameters>
        ^^
        ||
        ||
        ||
        ||
        ||
This Parameters should be passed on to the Function!
"""
@app.route("/error/<ErrorCode>")
def error(ErrorCode):
    return  "Error  : %s" % ErrorCode



"""
@BuradaVivek
app.run(host,port,options)

"""


if __name__ == "__main__":
    app.run(port=3000,debug = True)
else :
    print("Run By Main"+__name__)
