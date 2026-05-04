import sqlite3

#variable for database name
DATABASE = 'xxbestfoods.db'

#functions
def print_all_foods():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = 'SELECT * FROM best_foods'
    cursor.execute(sql)
    results = cursor.fetchall()
    print(results)

    db.close() \

#main code 
print_all_foods()