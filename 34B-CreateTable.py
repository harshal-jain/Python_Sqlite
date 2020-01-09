#!/usr/bin/python
import sqlite3

conn = sqlite3.connect('db_shriram.db')
print ("Opened database successfully")

#conn.execute("CREATE TABLE tbl_Company (CompanyId int PRIMARY KEY, CName  varchar(200), Age  int, Address  varchar(50), Salary REAL);")
conn.execute("CREATE TABLE IF NOT EXISTS tbl_Company (CompanyId int PRIMARY KEY, CName  varchar(200), Age  int, Address  varchar(50), Salary REAL);")
print ("Table created successfully")

conn.close()