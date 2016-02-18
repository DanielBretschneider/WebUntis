#!/usr/bin/env python3

"""
__author__ = "Daniel Bretschneider"
__version__ = "1.0.1"
__email__ = "dani.bretschneider@gmail.com"
__status__ = "(More or less) Finished."
"""

from datetime import date
import webuntis
import datetime
import WebUntis_Session

# session-setup [ID fuer 5DN: 365, 1AI: 350]
session = WebUntis_Session.open_session()

def logout():
    """
    logout(): closes the session.
    """
    session.logout()

def getSession():
    """
    getSession(): returns current session-object.
    """
    return session

def printDepartments():
    """
    printDepartments(): prints all departments inside the school.
    """
    print ("\n---> departments")

    for department in session.departments():
        print("id: %4d, name: %-5s, long_name: %s" % (department.id, department.name, department.long_name))


def getDepartments():
    """
    getDepartments(): returns all departments.
    """
    departments = []

    for department in session.departments():
        department = (department.id, department.name, department.long_name)
        departments.append(department)

    return departments

def printRooms():
    """
    printRooms(): prints all departments inside the school.
    """
    print ("\n---> rooms")

    for room in session.rooms():
        print("id: %d, name: %s, long_name: %s" % (room.id, room.name, room.long_name))


def getRooms():
    """
    getRooms(): returns all rooms.
    """
    rooms = []

    for room in session.rooms():
        room = (room.id, room.name, room.long_name)
        rooms.append(room)

    return rooms

def printHolidays():
    """
    printHolidays(): prints all the holidays, that occur.
    """
    print ("\n---> holidays")

    for holiday in session.holidays():
        print("id: %4d, start: %s, end: %s, name: %s, short_name: %s" %
              (holiday.id, holiday.start, holiday.end, holiday.name, holiday.short_name))

def getHolidays():
    """
    getHolidays(): returns all holidays.
    """
    holidays = []

    for holiday in session.holidays():
        holiday = (holiday.id, holiday.start, holiday.end, holiday.name, holiday.short_name)
        holidays.append(holiday)

    return holidays


def printClasses():
    """
    printClasses(): prints out all the available classes of the school. (short_name + name)
    """
    print ("\n---> klassen")

    for klasse in session.klassen():
        #print("id: %4d, name: %-5s, long_name: %s" % (klasse.id, klasse.name, klasse.long_name))
        print('%d;"%s";"%s"' % (klasse.id, klasse.name, klasse.long_name))

def getClasses():
    """
    getClasses(): returns all classes.
    """
    classes = []

    for cls in session.klassen():
        cls = (cls.id, cls.name, cls.long_name)
        classes.append(cls)

    return classes

def printSubjects():
    """
    printSubjects(): prints all departments inside the school.
    """
    print ("\n---> subjects")

    for subject in session.subjects():
        print("id: %d, name: %s, long_name: %s" % (subject.id, subject.name, subject.long_name))

def getSubjects():
    """
    getSubjects(): returns all subjects.
    """
    subjects = []

    for subj in session.subjects():
        subj = (subj.id, subj.name, subj.long_name)
        subjects.append(subj)

    return subjects

def printTeacher():
    """
    printSubjects(): prints all departments inside the school.
    """
    print ("\n---> teacher")

    for teacher in session.teachers():
        print("id: %d, name: %s, long_name: %s" % (teacher.id, teacher.name, teacher.long_name))

def getTeachers():
    """
    getTeachers(session): returns all teacher.
    """
    teacher = []

    for t in session.teachers():
        t = (teacher.id, teacher.name, teacher.long_name)
        teacher.append(t)

    return teacher

def getTeacher_shortname():
    """
    getTeacher(session): returns all teacher.
    """
    teacher = []

    for t in session.teachers():
        t = t.name
        teacher.append(t)

    return teacher

def printSchoolyears():
    """
    printSchoolyears(session): prints all departments inside the school.
    """
    print ("\n---> schoolyears")

    for schoolyear in session.schoolyears():
        print("id: %d, name: %s" % (schoolyear.id, schoolyear.name))

def getSchoolyears():
    """
    getSchoolyears(session): returns all available schoolyears.
    """
    schoolyears = []

    for sy in session.teachers():
        sy = (sy.id, sy.name)
        schoolyears.append(sy)

    return schoolyears

def printTimetable(id):
    """
    printTimetable(session, id): prints timetable of specified class on a dedicated date.
    """
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

def printSubstitutions():
    """
    printTimetable(session, id): prints timetable of specified class on a dedicated date.
    """
    print ("\n---> substitutions")

    today = date.today()
    monday = today - datetime.timedelta(days=today.weekday())
    friday = monday + datetime.timedelta(days=1)

    for substitute in session.substitutions(start=monday, end=friday, departmentId=0):
        if (substitute.reschedule_start == None):
            continue
        else :
            print("start: %s, end: %s, type: %s" % (substitute.reschedule_start, substitute.reschedule_end, substitute.type()))

def printSubstitutionForSpecificTeacher(teachername):
    """
    printSubstitutionsForSpecificTeacher(): returns any changes of specific timetables
    """
    lehrername=teachername
    start = datetime.date.today()
    end = start + datetime.timedelta(days=14)

    lehrer = session.teachers().filter(name=lehrername)[0]
    table = session.timetable(teacher=lehrer, start=start, end=end).to_table()

    EOL = "\n"

    res = ""
    res += "teacher: " + lehrername + EOL
    res += "start  : " + str(start) + EOL
    res += "end    : " + str(end) + EOL

    for time, row in table:
       timetext = '{}'.format(time.strftime('%H:%M'))
       for date, cell in row:
          for period in cell:
            if period.code:
                klassen = ', '.join(cls.name for cls in period.klassen)
                gegst = ', '.join(su.name for su in period.subjects)
                res += str(date) + " " + str(timetext) +  ": "
                res += gegst + " / "
                res += klassen + " / "
                res += period.code + EOL
    #print(res)
    return res

def getSubstitutionForSpecificTeacher(teachername):
    """
    getSubstitutionsForSpecificTeacher(): returns any changes of specific timetables
    """
    lehrername=teachername
    start = datetime.date.today()
    end = start + datetime.timedelta(days=14)

    lehrer = session.teachers().filter(name=lehrername)[0]
    table = session.timetable(teacher=lehrer, start=start, end=end).to_table()

    res = ""
    EOL = "\n"
    substitutionlist = []

    for time, row in table:
       timetext = '{}'.format(time.strftime('%H:%M'))
       for date, cell in row:
          for period in cell:
            if period.code:
                klassen = ', '.join(cls.name for cls in period.klassen)
                gegst = ', '.join(su.name for su in period.subjects)
                res += str(date) + " " + str(timetext) +  ": "
                res += gegst + " / "
                res += klassen + " / "
                res += period.code + EOL

    substitutionlist = res.split("\n")
    substitutionlist = filter(None, substitutionlist)
    return substitutionlist

def checkForSubstitutions():
    """
    checkForSubstitutions(): prints out every teacher with number ofsubstitions.
    :return:
    """
    teacherlist = getTeacher_shortname()

    for teacher in teacherlist:
        lst = getSubstitutionForSpecificTeacher(teacher)
        numOfSubstitutions = len(lst)
        if numOfSubstitutions == 1:
            print("'%s' has %d substitution!" % (teacher, numOfSubstitutions))
        elif numOfSubstitutions > 1:
            print("'%s' has %d substitutions!" % (teacher, numOfSubstitutions))
        else:
            print("'%s' has no substitutions!" % (teacher))

def printAllSubstitutions():
    """
    printAllSubstitutions(): Prints out all Substitutions of every teacher in the next two weeks. (test)
    :return:
    """
    allteachers = getTeacher_shortname()

    for t in allteachers:
        print(getSubstitutionForSpecificTeacher(t))

