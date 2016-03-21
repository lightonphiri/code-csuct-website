from sqlite3 import*
db=connect('Point of sale.db')
db.execute('create table if not exists Stock(stock_code text,item_name text,description text,cost_price real,sales_price real,quantity int,PRIMARY KEY(stock_code))')
db.execute('insert into Stock values("BAR","Bar one","chocolate",9.50,13.00,12)')
db.execute('insert into Stock values("RED","Red Bull", "Energy drink",12.00,16.00,25)')
db.execute('insert into Stock values("COKE","Coca-cola","Soft drink",9.00,13.50,25)')
db.execute('insert into Stock values("TEN","Tennis","Biscuits",7.20,11.00,30)')
db.execute('insert into Stock values("AQUA","Aquelle","Bottled water", 3.00,5.00,20)')
db.execute('insert into Stock values("BON","Bonaqua","Bottled water", 3.50,6.00,20)')
db.execute('insert into Stock values("CREAM","Lemons Creams","Biscuits",9.5,13.00,30)')
db.execute('insert into Stock values("SIM","Simba","Potato chips",8.50,12.00,35)')
db.execute('insert into Stock values("ORE","Oreo","Biscuits",8.50,12.00,35)')
db.execute('insert into Stock values("DOR","Doritos","Potato chips",8.50,12.00,35)')




db.commit()