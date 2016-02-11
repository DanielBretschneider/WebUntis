#!/usr/bin/env python3
__author__ = 'Daniel Bretschneider'

from WebUntisData import *

session = getSession()
id = 365

#printClasses(session)
#printDepartments(session)
#printRooms(session)
#printSubjects(session)
#printTeacher(session)
#printSchoolyears(session)
#printSubstitutions(session)
printTimetable(session, id)

logout()