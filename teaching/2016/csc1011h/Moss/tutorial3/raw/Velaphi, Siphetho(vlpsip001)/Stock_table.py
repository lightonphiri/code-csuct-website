import sqlite3

db = sqlite3.connect('Stock_table.db')
db.execute('create table Stock(Stock Code integer,Item Name text,Discription text,Cost Price real,Sales Price real,Quantity Stock integer)')
db.execute('insert into Stock values (?,?,?,?,?,?)',(1,'Banana','Each',5,3,20))
db.execute('insert into Stock values (?,?,?,?,?,?)',(2,'Apple','Each',4,2.50,20))
db.execute('insert into Stock values (?,?,?,?,?,?)',(3,'Guava','Each',2,1.50,20))
db.execute('insert into Stock values (?,?,?,?,?,?)',(4,'Peach','Each',3,2,20))
db.execute('insert into Stock values (?,?,?,?,?,?)',(5,'Mango','Each',9,11,20))
db.execute('insert into Stock values (?,?,?,?,?,?)',(6,'Pear','Each',4,2.50,20))
db.execute('insert into Stock values (?,?,?,?,?,?)',(7,'Orange','Each',2,1.50,20))
db.execute('insert into Stock values (?,?,?,?,?,?)',(8,'Cherry','Each',2,1.50,20))
db.execute('insert into Stock values (?,?,?,?,?,?)',(9,'Rasberry','Each',2,1.50,20))
db.execute('insert into Stock values (?,?,?,?,?,?)',(10,'Ovacado','Each',5,3,20))
db.commit()

