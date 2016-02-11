#!/usr/bin/env python3
from datetime import date

__author__ = 'Daniel Bretschneider'
import webuntis
import datetime

# session-setup [ID fuer 5DN: 365, 1AI: 350]
session = webuntis.Session(
    username='htl3r',
    password='htl3r',
    server='https://urania.webuntis.com',
    school='htl3r',
    useragent='Webuntis Test'
).login()

"""
logout() - closes the session.
"""
def logout():
    session.logout()

"""
getSession() - returns current session-object.
"""
def getSession():
    return session

"""
printDepartments(session) - prints all departments inside the school.
"""
def printDepartments(session):
    print ("\n---> departments")

    for department in session.departments():
        print("id: %4d, name: %-5s, long_name: %s" % (department.id, department.name, department.long_name))

"""
getDepartments(session) - returns all departments.
"""
def getDepartments(session):
    departments = []

    for department in session.departments():
        department = (department.id, department.name, department.long_name)
        departments.append(department)

    return departments

"""
printRooms(session) - prints all departments inside the school.
"""
def printRooms(session):
    print ("\n---> rooms")

    for room in session.rooms():
        print("id: %d, name: %s, long_name: %s" % (room.id, room.name, room.long_name))

"""
getRooms(session) - returns all rooms.
"""
def getRooms(session):
    rooms = []

    for room in session.rooms():
        room = (room.id, room.name, room.long_name)
        rooms.append(room)

    return rooms

"""
printHolidays(session) - prints all the holidays, that occur.
"""
def printHolidays(session):
    print ("\n---> holidays")

    for holiday in session.holidays():
        print("id: %4d, start: %s, end: %s, name: %s, short_name: %s" %
              (holiday.id, holiday.start, holiday.end, holiday.name, holiday.short_name))

"""
getHolidays(session) - returns all holidays.
"""
def getHolidays(session):
    holidays = []

    for holiday in session.holidays():
        holiday = (holiday.id, holiday.start, holiday.end, holiday.name, holiday.short_name)
        holidays.append(holiday)

    return holidays

"""
printClasses(session) - prints out all the available classes of the school. (short_name + name)
"""
def printClasses(session):
    print ("\n---> klassen")

    for klasse in session.klassen():
        #print("id: %4d, name: %-5s, long_name: %s" % (klasse.id, klasse.name, klasse.long_name))
        print('%d;"%s";"%s"' % (klasse.id, klasse.name, klasse.long_name))

"""
getClasses(session) - returns all classes.
"""
def getClasses(session):
    classes = []

    for cls in session.klassen():
        cls = (cls.id, cls.name, cls.long_name)
        classes.append(cls)

    return classes

"""
printSubjects(session) - prints all departments inside the school.
"""
def printSubjects(session):
    print ("\n---> subjects")

    for subject in session.subjects():
        print("id: %d, name: %s, long_name: %s" % (subject.id, subject.name, subject.long_name))


"""
getSubjects(session) - returns all subjects.
"""
def getSubjects(session):
    subjects = []

    for subj in session.subjects():
        subj = (subj.id, subj.name, subj.long_name)
        subjects.append(subj)

    return subjects

"""
printSubjects(session) - prints all departments inside the school.
"""
def printTeacher(session):
    print ("\n---> teacher")

    for teacher in session.teachers():
        print("id: %d, name: %s, long_name: %s" % (teacher.id, teacher.name, teacher.long_name))

"""
getTeacher(session) - returns all teacher.
"""
def getTeacher(session):
    teacher = []

    for t in session.teachers():
        t = (t.id, t.name, t.long_name)
        teacher.append(t)

    return teacher

"""
printSchoolyears(session) - prints all departments inside the school.
"""
def printSchoolyears(session):
    print ("\n---> schoolyears")

    for schoolyear in session.schoolyears():
        print("id: %d, name: %s" % (schoolyear.id, schoolyear.name))

"""
getSchoolyears(session) - returns all available schoolyears.
"""
def getSchoolyears(session):
    schoolyears = []

    for sy in session.teachers():
        sy = (sy.id, sy.name)
        schoolyears.append(sy)

    return schoolyears


"""
printTimetable(session, id) - prints timetable of specified class on a dedicated date.
"""
def printTimetable(session, id):
    print ("\n---> timetable")

    today = datetime.date.today()
    monday = today - datetime.timedelta(days=today.weekday())
    friday = monday + datetime.timedelta(days=4)

    klasse = session.klassen().filter(id=id)[0]
    timetable = session.timetable(klasse=klasse, start=monday, end=friday)

    ttable = []
    for tt in timetable:
        for klasse in tt.klassen:
            #k.append(klasse.name)
            ttable.append("id: %4d, subject: %s, start: %s, end: %s, klasse: %s" % (
                tt.id, tt.subjects , tt.start, tt.end, klasse))

    for line in ttable:
        print(line)

"""
printTimetable(session, id) - prints timetable of specified class on a dedicated date.
"""
def printSubstitutions(session):
    print ("\n---> substitutions")

    today = date.today()
    monday = today - datetime.timedelta(days=today.weekday())
    friday = monday + datetime.timedelta(days=1)

    for substitute in session.substitutions(start=monday, end=friday, departmentId=0):
        if (substitute.reschedule_start == None):
            continue
        else :
            print("start: %s, end: %s, type: %s" % (substitute.reschedule_start, substitute.reschedule_end, substitute.type()))

"""
getSubstitutions(session) - ...
"""
def getSubstitutions(session):
    substitutions=[]
    id=0

    today = date.today()
    monday = today - datetime.timedelta(days=today.weekday())
    friday = monday + datetime.timedelta(days=1)

    for substitute in session.substitutions(start=monday, end=friday, departmentId=0):
        if (substitute.reschedule_start == None):
            continue
        else :
            id=id+1
            substitute = (id, substitute.reschedule_start, substitute.reschedule_end, substitute.type())
            substitutions.append(substitute)

    return substitutions