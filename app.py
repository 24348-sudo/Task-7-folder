import sqlite3

db = sqlite3.connect('xxbestfoods.db')
cursor = db.cursor()
sql = 'SELECT * FROM best_foods'
cursor.execute(sql)
results = cursor.fetchall()
print(results)

db.close() 
