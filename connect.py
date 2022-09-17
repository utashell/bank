import sqlite3 as sq
con = sq.connect('C:/Users/sadaf/Desktop/project/bank.db')
print('ok')
c = con.cursor()
com = """create table user(
        id_user integer primary key,
        firstname Text(20),
        lastname Text(30),
        middle_name Text(20) ,
        age integer,
        gender Text(8),
        city Text(20),
        country Text(20),
        phone_number integer(11),
        email Text(40),
        address Text(50),
        username Text(20),
        password Text(20),
        account_num integer,
        date_account Text(50))"""
try:
    c.execute(com)
    con.commit()
except:
    print('error')
    con.rollback()

con.close()

