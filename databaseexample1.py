
from MySQLdb import connect

db = connect(host="localhost",user="root",password="mysql",db="employees")

cur = db.cursor()

cur.execute("select * from employee")

for r in cur.fetchall():
    print(r)

db.close()
