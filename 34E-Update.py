#!/usr/bin/python

import sqlite3

conn = sqlite3.connect('db_shriram.db')
print ("Opened database successfully")

#conn.execute("CREATE TABLE tbl_Test (CompanyId int PRIMARY KEY, CName  varchar(200));")
conn.execute("CREATE TABLE IF NOT EXISTS tbl_Test (CompanyId int PRIMARY KEY, CName  varchar(200));")
print ("Table created successfully")

id=input("Enter Id")
name=input("Enter name")

conn.execute("UPDATE tbl_Test SET CName='"+name+"' where CompanyId="+id);
conn.commit()

cursor = conn.execute("SELECT CompanyId,CName from tbl_Test")
for row in cursor:
   print ("CompanyId = ", row[0])
   print("CName = ", row[1], "\n")

print ("Operation done successfully")
conn.close()


conn.close()
