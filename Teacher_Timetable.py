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

# WebUntis Session opening
WEBUNTIS_SESSION = WebUntisData.getSession()

# List of all teachers of our school (as shortname, f.e. HAG)
TEACHERS = WebUntisData.getTeacher_shortname()

# Specific teacher id [38: HAG]
TEACHER_ID = 38

# todays date and monday+friday of the current week
today = datetime.date.today()
monday = today - datetime.timedelta(days=today.weekday())
friday = monday + datetime.timedelta(days=4)

# Create a timetable with type_id 2 (teacher) and teacher_id 38
table = WEBUNTIS_SESSION.timetable(teacher=TEACHER_ID, start=monday, end=friday).to_table()

def print_html_table():
    """
    print_html_table(): prints out the html code to display the timetable in a browser.
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

