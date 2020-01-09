#!/usr/bin/python

import sqlite3

conn = sqlite3.connect('db_shriram.db')
print ("Opened database successfully")

conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (1, 'Paul', 32, 'California', 20000.00 )");

conn.commit()
print ("Records created successfully")
conn.close()