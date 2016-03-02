#!/usr/bin/env python3

"""
__author__ = "Daniel Bretschneider"
__version__ = "1.0.1"
__email__ = "dani.bretschneider@gmail.com"
__status__ = "no status, just a test file."
"""
import WebUntis_Session
import WebUntisData

session = WebUntis_Session.open_session()
id = 365

#WebUntisData.printClasses()
#printDepartments()
#printRooms()
#printSubjects()
WebUntisData.printTeacher()
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