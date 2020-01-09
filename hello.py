#!/usr/bin/python

import sqlite3

conn = sqlite3.connect('db_shriram.db')
print ("Opened database successfully")

#conn.execute("CREATE TABLE tbl_Company (CompanyId int PRIMARY KEY, CName  varchar(200), Age  int, Address  varchar(50), Salary REAL);")
conn.execute("CREATE TABLE IF NOT EXISTS tbl_Company (CompanyId int PRIMARY KEY, CName  varchar(200), Age  int, Address  varchar(50), Salary REAL);")
print ("Table created successfully")


# conn.execute("INSERT INTO tbl_Company (CompanyId,CName,Age,Address,Salary) \
#       VALUES (2, 'Paul', 32, 'California', 20000.00 )");
# conn.commit()
#

cursor = conn.execute("SELECT CompanyId,CName,Age,Address,Salary from tbl_Company")
for row in cursor:
   print ("CompanyId = ", row[0])
   print("CName = ", row[1])
   print("Age = ", row[2])
   print ("Address = ", row[3])
   print ("Salary = ", row[4], "\n")

print ("Operation done successfully")
conn.close()


conn.close()