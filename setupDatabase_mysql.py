#!/usr/bin/env python3
__author__ = 'Daniel Bretschneider'

import MySQLdb

# MYSQL connection
connection = ""
cursor = ""

# all connection relevant parameters
mysql_user='root'
mysql_password=''
mysql_db_name='WebUntis-Data'
mysql_host='127.0.0.1'
mysql_port=3306

# tables to create
t_classes = "t_classes";
t_teacher = "t_teacher";
t_departments = "t_departments";
t_holidays = "t_holidays";

"""
connect() - connects to local database (WebUntis-Data).
"""
def connect():
    connection = MySQLdb.connect(user=mysql_user, passwd=mysql_password, db=mysql_db_name,
                             host=mysql_host, port=mysql_port)
    cursor = connection.cursor()

"""
createBasicDBLayout() - creates the fundamental layout of the database.
"""
def createBasicDBLayout():
    createTable(t_classes)
    createTable(t_teacher)
    createTable(t_departments)
    createTable(t_holidays)

"""
Method for the statement execution.
"""
def execute_statement(sql_cmd):
    cursor.execute(sql_cmd)
    connection.commit()

"""
createTable(t_name) - creates a mysql-table.
"""
def createTable(t_name):
    statement = "" \
      "CREATE TABLE %s(" \
      "ID int NOT NULL AUTO_INCREMENT PRIMARY KEY," \
      "shortname varchar(10) NOT NULL," \
      "longname varchar(50) NOT NULL)" % (t_name);
    cursor.execute(statement)


"""
dropTable() - drops specific table in database.
"""
def dropTable(t_name):
    statement = "drop table %s;" % (t_name)
    execute_statement(statement)


"""
printTableContent() - print content of specific table.
"""
def printTableContent(table_name):
    statement = "select * from %s;" % (table_name);
    execute_statement(statement)
    data = cursor.fetchall()
    for row in data:
        print (row[1], row[2])

"""
deconnect() - closes connection to database.
"""
def deconnect():
    connection.close()
