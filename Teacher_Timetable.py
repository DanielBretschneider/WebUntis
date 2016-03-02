#! /usr/bin/env python3

"""
__author__ = "Daniel Bretschneider"
__version__ = "1.0.1"
__email__ = "dani.bretschneider@gmail.com"
__status__ = "started"
"""

#
# This is a special program. Goal is to successfully display the timetable of our head of department Mr. Hager, as an html table.
# For the beginning. Next a database has to be created, so that the real data can be stored and managed, and later on displayed on
# the EPaper-Display in front of his room.
#

import WebUntis_Session
import WebUntisData
import datetime
import sqlite3

# WebUntis Session opening
WEBUNTIS_SESSION = WebUntisData.getSession()

# List of all teachers of our school (as shortname, f.e. HAG)
TEACHERS = WebUntisData.getTeacher_shortname()

# Specific teacher id [38: HAG]
TEACHER_ID = 38

# newline
EOL = "\n"

# database filename
DATABASE = "headOfDepartment.db"
CONNECTION = sqlite3.connect(DATABASE)

# todays date and monday+friday of the current week
today = datetime.date.today()
monday = today - datetime.timedelta(days=today.weekday())
friday = monday + datetime.timedelta(days=4)

# Create a timetable with type_id 2 (teacher) and teacher_id 38
table = WEBUNTIS_SESSION.timetable(teacher=TEACHER_ID, start=monday, end=friday).to_table()

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

def get_timetable_data():
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

def create_database():
    """
    create_database(): Creates the sqlite database and stores the information in it.
    :return:
    """
    # create or open database
    print("Opened database successfully")

def execute(statement):
    """
    execute(statement): executes sqlite-statement
    """
    CONNECTION.execute(statement)

def fill_database():
    """
    fill_database(): Fill information in database
    :return:
    """
    counter=0
    for d in get_timetable_data():
        counter+=1
        splitted=d.split(";")
        if len(splitted) is 1:
            break
        ins_schoolyears = "INSERT INTO timetable(ID, Date, Time, Subject, Class, Room, Substitution) " \
                          "VALUES(%d,'%s','%s','%s','%s','%s','%s');" % (counter, splitted[0], splitted[1],splitted[2],splitted[3],splitted[4], "No")
        execute(ins_schoolyears)


#
# Program Sequence
#
create_database()

# create table for Mr. Hager
create_t_timetable="CREATE TABLE IF NOT EXISTS timetable(" \
                   "ID              INTEGER PRIMARY KEY AUTOINCREMENT," \
                   "Date            VARCHAR(20) NOT NULL," \
                   "Time            VARCHAR(10) NOT NULL," \
                   "Subject         VARCHAR(10) NOT NULL," \
                   "Class           VARCHAR(10) NOT NULL," \
                   "Room            VARCHAR(10) NOT NULL," \
                   "Substitution    VARCHAR(10) NOT NULL);" \

# create table inside our database
execute(create_t_timetable)

# Fill DB.
fill_database()

# Close all sessions.
CONNECTION.commit()
CONNECTION.close()
WebUntis_Session.close_session(WEBUNTIS_SESSION)
