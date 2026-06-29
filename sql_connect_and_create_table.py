"""
MySQL Connection
"""
import mysql.connector

conn = mysql.connector.connect(
host='localhost',               # localhost
port='3306',
user='root',
password='1234',
database='flipkart'
    )
cur = conn.cursor()

#======================================================================

"""
sql = 'show databases'
cur.execute(sql)
print(cur.fetchall())


sql = 'create database flipkart'
cur.execute(sql)



sql = "use flipkart"
cur.execute(sql)
sql = '''
create table employee(
eid INT PRIMARY KEY AUTO_INCREMENT ,
ename VARCHAR(100) NOT NULL ,
eadd VARCHAR(100) NOT NULL ,
esal DECIMAL(10,2) NOT NULL 
)
'''
cur.execute(sql)



sql = 'insert into employee value(103,"Anu Singh","Delhi",76520)'
cur.execute(sql)





ename = input("Enter New Employee Name : ")
eadd = input("Enter Address : ")
esal = input("Enter Salary : ")
sql = 'insert into employee(ename,eadd,esal) value("'+ename+'","'+eadd+'",'+esal+')'
cur.execute(sql)
if cur.rowcount>0:
    print("Data Inserted Successfully!")
else:
    print("Failed to insert data")



ename = input("Enter New Employee Name : ")
eadd = input("Enter Address : ")
esal = input("Enter Salary : ")
sql = f'insert into employee(ename,eadd,esal) value("{ename}","{eadd}",{esal})'
cur.execute(sql)
if cur.rowcount>0:
    print("Data Inserted Successfully!")
else:
    print("Failed to insert data")



ename = input("Enter New Employee Name : ")
eadd = input("Enter Address : ")
esal = input("Enter Salary : ")
sql = 'insert into employee(ename,eadd,esal) value(%s,%s,%s)'
data = (ename,eadd,esal)
cur.execute(sql,data)
if cur.rowcount>0:
    print("Data Inserted Successfully!")
else:
    print("Failed to insert data")



query = "select * from employee"
cur.execute(query)
print( cur.fetchall() )



"""


query = "select * from employee"
cur.execute(query)
data = cur.fetchall()
for emp in data:
    print("Empoyee ID :",emp[0])
    print("Empoyee Name :",emp[1])
    print("Empoyee Address :",emp[2])
    print("Empoyee Salary :",emp[3])
    print("-----------------------------------")

#======================CLOSE MYSQL CONNECTION==========================
conn.commit()  # for permanent save
cur.close()
conn.close()
