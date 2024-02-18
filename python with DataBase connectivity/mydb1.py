import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",password='admin',database='project')
print("Connection stablised.\nConnection id is -",mydb.connection_id)
cur=mydb.cursor()
que='insert into book (book_id,titel,price) values(%s,%s,%s)'
books=[(2,"php",248),(3,"c",330),(4,"java",560)]
cur.executemany(que,books)
mydb.commit()
