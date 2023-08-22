import mysql.connector

mydb = mysql.connector.connect(host="localhost",user="root",password="Sagilk@2000",port=3306)
print(mydb)

mycursur = mydb.cursor()
mycursur.execute("create database bank")
# mycursur.execute("use maypython")
# # mycursur.execute("create table students(name varchar(20),age int,course varchar(50))")
# sql = "insert into students(name,age,course)values(%s, %s ,%s)"
# val = ("sagil",23,"python")
# mycursur.execute(sql,val)
# mydb.commit()
# print(mycursur.rowcount,"1 record inserted")
