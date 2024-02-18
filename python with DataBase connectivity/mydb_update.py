import mysql.connector
mydb=mysql.connector.connect(host="localhost",
                             user="root",
                             password='admin',
                             database='project')
print("Connection stablised.\nConnection id is -",mydb.connection_id)
cur=mydb.cursor()
s="update book set price=price+10 where price>335"
cur.execute(s)
mydb.commit()