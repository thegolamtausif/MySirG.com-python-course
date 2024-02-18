import mysql.connector
mydb=mysql.connector.connect(host="localhost",
                             user="root",
                             password='admin',
                             database='project')
print("Connection stablised.\nConnection id is -",mydb.connection_id)
cur=mydb.cursor()
s='delete from book where book_id=3'
cur.execute(s)
mydb.commit()