import sqlite3

con = sqlite3.connect('srini.db')
con.execute("CREATE TABLE IF NOT EXISTS srini (ID INTEGER PRIMARY KEY AUTOINCREMENT, NAME TEXT, AGE INTEGER, GENDER TEXT, CITY TEXT);")

def insertdata(NAME, AGE, GENDER, CITY):
    qry = "INSERT INTO srini (NAME, AGE, GENDER, CITY) VALUES (?, ?, ?, ?);"
    con.execute(qry, (NAME, AGE, GENDER, CITY))
    con.commit()
    print("srini detail added")

def updatedata(NAME, AGE, GENDER, CITY, Id):
    qry = "UPDATE srini SET NAME=?, AGE=?, GENDER=?, CITY=? WHERE ID=?;"
    con.execute(qry, (NAME, AGE, GENDER, CITY, Id))
    con.commit()
    print("srini detail updated")

def deletedata(Id):
    qry = "DELETE FROM srini WHERE ID=?; "
    con.execute(qry, (Id,))
    con.commit()
    print("srini detail deleted")

def selectdata():
    qry = "SELECT * FROM srini;"
    result = con.execute(qry)
    for row in result:
        print(row)

print("""
1. insert
2. update
3. delete
4. select
""")

choice = 1
while choice == 1:
    c = int(input("///ENTER YOUR CHOICE///"))

    if c == 1:
        print("**ADD NEW RECORD**")
        NAME = input("ENTER YOUR NAME")
        AGE = input("ENTER YOUR AGE")
        GENDER = input("ENTER YOUR GENDER")
        CITY = input("ENTER YOUR CITY")
        insertdata(NAME, AGE, GENDER, CITY)

    elif c == 2:
        print("**EDIT A RECORD***")
        Id = input("ENTER YOUR ID")
        NAME = input("ENTER YOUR NAME")
        AGE = input("ENTER YOUR AGE")
        GENDER = input("ENTER YOUR GENDER")
        CITY = input("ENTER YOUR CITY")
        updatedata(NAME, AGE, GENDER, CITY, Id)

    elif c == 3:
        print("**RECORD DELETED**")
        Id = input("ENTER ID: ")
        deletedata(Id)

    elif c == 4:
        print("ALL RECORDS: ")
        selectdata()

    else:
        print("INVALID SELECTION")

    choice = int(input("ENTER 1 TO CONTINUE"))

print("thank you////")
