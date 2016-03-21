import sqlite3

conn=sqlite3.connect("Sale.db")
c=conn.cursor()

def table():
    c.execute("CREATE TABLE IF NOT EXISTS sale(Stock code INT,Quantity INT,Time TXT,Date TXT)")
    conn.commit()
    c.close()
table()    