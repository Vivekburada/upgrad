# Basic E commerce App

## Search Algorithm

 In order to achieve Search Functionalities I have created a sqlite3 DATABASE with index of product and all possible Keyword Mappings

```
 "select * from DATA where DUMP like ? order by RANDOM()",
         ('%'+Keyword+'%',)"
```
Here when ever we search for a Keyword for example bags that are "waterproof" , then above code searches that
Columns that have words **LIKE**  "waterproof" and sends them. Column containing Keywords for the product are **case insensitive hence  waterproof, Waterproof WATerproof all points to same column that consists that keyword.  

This code selects all columns that consists  that **keyword** and then **ORDERS** them randomly. So every time you make a request for **Backpack** you possibly get different product which is a backpack!

I haven't handled when the requested keyword is not found. But logs **"ERROR 400"** in console.
```
1 ======> 'LOUIS CARON Stylish 15.6 waterproof laptop Backpack 25 L Backpack  (Red, Purple) Men  Women 15.6 17 18, 19 25 L 25L  Polyester'
```  
##  COOKIES

There hasn't much done in order to validate login and logout. I simple story a cookie of username when user logins in.

Hence please don't logout otherwise most things don't work which requires  **username** [EMAIL].  

## SQLITE3

If DATABASE is not present then it only populates the database.

**users.db** stores user details Email ID and Password.

**data.db** stores index of product and keyword dump.  

Please mail me for any queries: vivekburada97@gmail.com
