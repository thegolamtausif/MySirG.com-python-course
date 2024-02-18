import mysql.connector
mydb=mysql.connector.connect(host="localhost",
                             user="root",
                             password='admin',
                             database='project')
print("Connection stablised.\nConnection id is -",mydb.connection_id)
cur=mydb.cursor()
s="select * from book"
cur.execute(s)
result=cur.fetchall()
for rec in result:
    print(rec)
    