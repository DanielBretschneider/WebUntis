#!/usr/bin/env python3

"""
__author__ = "Daniel Bretschneider"
__version__ = "1.0.1"
__email__ = "dani.bretschneider@gmail.com"
__status__ = "no status, just a test file."
"""

#
# This is just a testing-file and is not a relevant script of our diploma project.
#

import WebUntis_Session
import WebUntisData
import datetime
import json
import re

session = WebUntis_Session.open_session()
id = 365

#WebUntisData.printClasses()
#printDepartments()
#printRooms()
#printSubjects()
print(WebUntisData.getTeacherID("BRE"))
#printSchoolyears()
#printSubstitutions()
#printTimetable(id)
#print(getSubstitutions())
#print(WebUntisData.getClasses())
#WebUntisData.printAllSubstitutions()
#x = WebUntisData.getSubstitutionForSpecificTeacher("KOR")

#print(WebUntisData.printSubstitutionForSpecificTeacher("KOR"))
#WebUntisData.printAllSubstitutions()
#WebUntisData.checkForSubstitutions()

WebUntis_Session.close_session(session)