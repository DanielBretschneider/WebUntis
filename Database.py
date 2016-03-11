#! /usr/bin/env python3

"""
__author__ = "Daniel Bretschneider"
__version__ = "1.0.1"
__email__ = "dani.bretschneider@gmail.com"
__status__ = "started"
"""

#
# Creates the database, including every teacher with his timetable.
#

import WebUntis_Session
import WebUntisData
import datetime
import os
import sqlite3

# WebUntis Session opening
WEBUNTIS_SESSION = WebUntisData.getSession()

# List of all teachers of our school (as shortname, f.e. HAG)
TEACHERS = WebUntisData.getTeacher_shortname()

# newline
EOL = "\n"

# database filename - and check if file exists
# if file exists, delete it
DATABASE = "untis.db"

# todays date and monday+friday of the current week
today = datetime.date.today()
monday = today - datetime.timedelta(days=today.weekday())
friday = monday + datetime.timedelta(days=4)

def print_html_table():
    """
    print_html_table(): prints out the html code to display the timetable in a browser.(will probably stay unused)
    :return: nothing..
    """
    print('<table border="1"><thead><th>Time</th>')
    for weekday in ['Montag', 'Dienstag', 'Mittwoch', 'Donnerstag', 'Freitag']:
        print('<th>' + str(weekday) + '</th>')

    print('</thead><tbody>')
    for time, row in table:
        print('<tr>')
        print('<td>{}</td>'.format(time.strftime('%H:%M')))
        for date, cell in row:
            print('<td>')
            for period in cell:
                print(', '.join(su.name for su in period.subjects))
            print('</td>')
        print('</tr>')
    print('</tbody></table>')

def get_timetable_data(table):
    """
    get_timetable_data(): get Hagers timetable data for the storing inside his database.
    :return:
    """
    res=""

    for time, row in table:
       timetext = '{}'.format(time.strftime('%H:%M'))
       for date, cell in row:
          for period in cell:
            klassen = ', '.join(cls.name for cls in period.klassen)
            gegst = ', '.join(su.name for su in period.subjects)
            raum = ', '.join(su.name for su in period.rooms)
            res += str(date) + ";" + str(timetext +  ";")
            res += gegst + ";"
            res += klassen + ";"
            res += raum + ";"
            res += EOL

    data = res.split(EOL)
    return data

def print_data_formatted():
    """
    print_data_formatted(): print out data line-by-line.
    :return:
    """
    for line in get_timetable_data():
        print line

def createDatabase():
    """
    create_database(): Creates the sqlite database and stores the information in it.
    :return:
    """
    # create or open database
    if (os.path.exists(DATABASE)):
        os.remove(DATABASE)

    print("Opened database successfully")

def execute(statement):
    """
    execute(statement): executes sqlite-statement
    """
    CONNECTION.execute(statement)

def createTeacherTables():
    """
    createTeacherTables(): creates a table in db for every teacher.
    :return:
    """
    for teacher in TEACHERS:
        create_t_timetable="CREATE TABLE IF NOT EXISTS t_" + teacher + " (" \
        "ID              INTEGER PRIMARY KEY AUTOINCREMENT," \
        "Date            VARCHAR(20) NOT NULL," \
        "Time            VARCHAR(10) NOT NULL," \
        "Subject         VARCHAR(10) NOT NULL," \
        "Class           VARCHAR(10) NOT NULL," \
        "Room            VARCHAR(10) NOT NULL," \
        "Substitution    VARCHAR(10) NOT NULL);"
        execute(create_t_timetable)

def fillTables():
    """
    fillTables(): loads timetable in database.
    :return:
    """
    counter=0
    for te in TEACHERS:
        id = WebUntisData.getTeacherID(te)
        print(u"Teacher '"+te+"' with id '"+str(id)+"' :: table created")
        table = WEBUNTIS_SESSION.timetable(teacher=id, start=monday, end=friday).to_table()

        for d in get_timetable_data(table):
            counter+=1
            splitted=d.split(";")
            if len(splitted) is 1:
                break
            insertCMD = "INSERT INTO t_%s(ID, Date, Time, Subject, Class, Room, Substitution) " \
                        "VALUES(%d,'%s','%s','%s','%s','%s','%s');" % (te, counter, splitted[0], splitted[1],splitted[2],splitted[3],splitted[4], "No")
            execute(insertCMD)

#
# Program Sequence
#
createDatabase()
CONNECTION = sqlite3.connect(DATABASE)
createTeacherTables()
fillTables()

# Close all sessions.
CONNECTION.commit()
CONNECTION.close()
WebUntis_Session.close_session(WEBUNTIS_SESSION)
