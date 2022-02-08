# -*- coding: utf-8 -*-
S

from tkinter import *
import sys
#import mysql.connector as MySQLdb
import pymysql as MySQLdb
 
conn = MySQLdb.connect (host ="localhost",user = "root",passwd = "",db = "test")
cursor = conn.cursor () 
#cursor.execute("selectS * from maindb")
  
def SaveData():
    f = a.get()
    g = b.get()
    #cursor.execute ("DROP TABLE IF EXISTS maindb")
    #cursor.execute ("CREATE TABLE maindb(fname VARCHAR(20), lname VARCHAR(20))")
    cursor.execute ("INSERT INTO maindb(fname, lname) VALUES(%s, %s)", [f,g])
    print("Number of rows inserted: %d" % cursor.rowcount)
    if(cursor.rowcount==1):
        print("Record inserted")
    else:
        print("Record not inserted")
    conn.commit()
    
def FetchData():
    data=cursor.fetchone()
    name.set(data[0])
    lname.set(data[1])
   
       
 
root = Tk()
 
ent_frame = Frame(root)
Label(ent_frame, text="FIRST NAME:").pack(side=LEFT)
name=StringVar()
a = Entry(ent_frame,textvariable=name, width=15)
a.pack(side=LEFT)
Label(ent_frame, text="LAST NAME:").pack(side=LEFT)
lname=StringVar()
b = Entry(ent_frame,textvariable=lname, width=15)
b.pack(side=LEFT)
ent_frame.pack()
 
Button(root, text="insert",command=SaveData).pack(side=LEFT)
Button(root, text="Next record",command=FetchData).pack(side=LEFT)
Button(root, text="update").pack(side=LEFT)
Button(root, text="delete").pack(side=LEFT)
 
mainloop()
 
 