#!/usr/bin/env python3

"""
__author__ = "Daniel Bretschneider"
__version__ = "1.0.1"
__email__ = "dani.bretschneider@gmail.com"
__status__ = "(More or less) Finished."
"""
import WebUntis_Session
import WebUntisData

session = WebUntis_Session.open_session()
id = 365

#WebUntisData.printClasses()
#printDepartments()
#printRooms()
#printSubjects()
#printTeacher()
#printSchoolyears()
#printSubstitutions()
#printTimetable(id)
#print(getSubstitutions())
#WebUntisData.printAllSubstitutions()
#x = WebUntisData.getSubstitutionForSpecificTeacher("KOR")

#print(WebUntisData.printSubstitutionForSpecificTeacher("KOR"))
WebUntisData.printAllSubstitutions()
#WebUntisData.checkForSubstitutions()

WebUntis_Session.close_session(session)