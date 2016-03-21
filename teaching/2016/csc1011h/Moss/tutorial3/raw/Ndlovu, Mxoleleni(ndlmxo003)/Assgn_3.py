import sqlite3

stock = sqlite3.connect("All_Stock.db")
stock.execute("insert into Stock values (?,?,?,?,?,?)",(1,"washing soap","for laundry",18,20,15))

stock.commit()

print(stock)