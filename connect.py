# -*- coding: utf-8 -*-


#import mysql.connector as my
import pymysql as my


db = my.connect(host="127.0.0.1",user="root",passwd="",db="demo")

#print(db)
 
cursor = db.cursor()
 
#print(cursor)

cursor.execute( "SELECT id,name, age FROM table1" )

for id,name, age in cursor.fetchall() :
          print(id,name, age)
        
# # cursor.execute("SELECT VERSION()")

# # # # # Fetch a single row using fetchone() method.
# # # # #data = cursor.fetchone()
# # # # #print("Database version : %s " % data)

cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

# Create table as per requirement
sql = "CREATE TABLE EMPLOYEE (FIRST_NAME  CHAR(20) NOT NULL,LAST_NAME  CHAR(20),AGE INT,SEX CHAR(1),INCOME FLOAT )"

cursor.execute(sql)


sql = "INSERT INTO EMPLOYEE(FIRST_NAME,LAST_NAME, AGE, SEX, INCOME)VALUES ('Mac', 'Mohan', 20, 'M', 2000)"
try:
    # Execute the SQL command
    cursor.execute(sql)
    # Commit your changes in the database
    db.commit()
except:
#     # Rollback in case there is any error
    db.rollback()


# # # # Prepare SQL query to UPDATE required records
sql = "UPDATE EMPLOYEE SET AGE = AGE+1 WHERE SEX = '%c'" % ('M')
try:
    # Execute the SQL command
    cursor.execute(sql)
#     # Commit your changes in the database
    db.commit()
except:
#     # Rollback in case there is any error
    db.rollback()

# # # # Prepare SQL query to DELETE required records


sql = "DELETE FROM EMPLOYEE WHERE AGE > '%d'" % (20)
try:
#     # Execute the SQL command
    cursor.execute(sql)
#     # Commit your changes in the database
    db.commit()
except:
#     # Rollback in case there is any error
    db.rollback()
        
cursor.close()

