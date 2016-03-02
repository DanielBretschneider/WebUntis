#!/usr/bin/env python3
__author__ = 'Daniel Bretschneider'

import sqlite3
import WebUntis_Session
import WebUntisData

# WebUntis session
session = WebUntis_Session.open_session()

# name of the database / database file
n_database = "WebUntis.db"

# create or open database
conn = sqlite3.connect(n_database)
print("Opened database successfully")

def execute(statement):
    """
    execute(statement): executes sqlite-statement
    """
    conn.execute(statement)

# create table for classes
create_t_classes = "CREATE TABLE IF NOT EXISTS classes(" \
                   "ID              INTEGER PRIMARY KEY AUTOINCREMENT," \
                   "SHORT_NAME      VARCHAR(50) NOT NULL," \
                   "LONG_NAME       VARCHAR(70) NOT NULL);"

# create table for rooms
create_t_rooms = "CREATE TABLE IF NOT EXISTS rooms(" \
                   "ID              INTEGER PRIMARY KEY AUTOINCREMENT," \
                   "SHORT_NAME      VARCHAR(50) NOT NULL," \
                   "LONG_NAME       VARCHAR(70) NOT NULL);"

# create table for department
create_t_department = "CREATE TABLE IF NOT EXISTS departments(" \
                   "ID              INTEGER PRIMARY KEY AUTOINCREMENT," \
                   "SHORT_NAME      VARCHAR(50) NOT NULL," \
                   "LONG_NAME       VARCHAR(70) NOT NULL);"

# create table for subjects
create_t_subjects = "CREATE TABLE IF NOT EXISTS subjects(" \
                   "ID              INTEGER PRIMARY KEY AUTOINCREMENT," \
                   "SHORT_NAME      VARCHAR(50) NOT NULL," \
                   "LONG_NAME       VARCHAR(70) NOT NULL);"

# create table for teacher
create_t_teacher = "CREATE TABLE IF NOT EXISTS teacher(" \
                   "ID              INTEGER PRIMARY KEY AUTOINCREMENT," \
                   "SHORT_NAME      VARCHAR(50) NOT NULL," \
                   "LONG_NAME       VARCHAR(70) NOT NULL);"

# create table for holidays
create_t_holidays = "CREATE TABLE IF NOT EXISTS holidays(" \
                    "ID              INTEGER PRIMARY KEY AUTOINCREMENT," \
                    "START           VARCHAR(50) NOT NULL," \
                    "END             VARCHAR(50) NOT NULL," \
                    "NAME            VARCHAR(50) NOT NULL," \
                    "SHORT_NAME      VARCHAR(50) NOT NULL);"

# create table for schoolyears
create_t_schoolyears =  "CREATE TABLE IF NOT EXISTS schoolyears(" \
                        "ID        INTEGER PRIMARY KEY AUTOINCREMENT," \
                        "NAME      VARCHAR(50) NOT NULL);"

# create table for schoolyears
create_t_substitutions =  "CREATE TABLE IF NOT EXISTS substitutions(" \
                          "ID        INTEGER PRIMARY KEY AUTOINCREMENT," \
                          "START     VARCHAR(50) NOT NULL," \
                          "END       VARCHAR(50) NOT NULL);"


def loadClasses():
    """
    loadClasses(): load all classes into database
    """
    classes = WebUntisData.getClasses()

    for classes in classes:
        ins_classes =  "INSERT INTO classes(ID, SHORT_NAME, LONG_NAME) VALUES(%4d, '%-5s', '%s');" % (classes[0], classes[1], classes[2])
        execute(ins_classes)

def loadDepartments():
    """
    loadDepartments(): load all departements into database
    """
    departments = WebUntisData.getDepartments()

    for dep in departments:
        ins_departments = "INSERT INTO departments(ID, SHORT_NAME, LONG_NAME) " \
                          "VALUES(%d, '%-5s', '%s');" % (dep[0], dep[1], dep[2])
        execute(ins_departments)

def loadRooms():
    """
    loadRooms(): load all rooms into database
    """
    rooms = WebUntisData.getRooms()

    for room in rooms:
        ins_rooms = "INSERT INTO rooms(ID, SHORT_NAME, LONG_NAME) " \
                          "VALUES(%d, '%-5s', '%s');" % (room[0], room[1], room[2])
        execute(ins_rooms)

def loadSubjects():
    """
    loadSubjects(): load all subjects into database
    """
    subjects = WebUntisData.getSubjects()

    for subj in subjects:
        ins_subjects = "INSERT INTO subjects(ID, SHORT_NAME, LONG_NAME) " \
                          "VALUES(%d, '%-5s', '%s');" % (subj[0], subj[1], subj[2])
        execute(ins_subjects)

def loadTeacher():
    """
    loadTeacher(): load all teacher into database
    """
    teacher = WebUntisData.getTeachers()

    for t in teacher:
        ins_teacher = "INSERT INTO teacher(ID, SHORT_NAME, LONG_NAME) " \
                          "VALUES(%d, '%-5s', '%s');" % (t[0], t[1], t[2])
        execute(ins_teacher)

def loadSchoolyears():
    """
    loadSchoolyears(): load all schoolyears into database
    """
    schoolyears = WebUntisData.getSchoolyears()

    for sy in schoolyears:
        ins_schoolyears = "INSERT INTO schoolyears(ID, NAME) " \
                          "VALUES(%d, '%s');" % (sy[0], sy[1])
        execute(ins_schoolyears)


def loadHolidays():
    """
    loadHolidays(): load all holidays into database
    """
    holidays = WebUntisData.getHolidays()

    for holiday in holidays:
        ins_holidays = "INSERT INTO holidays(ID, START, END, NAME, SHORT_NAME) " \
                          "VALUES(%4d, '%s', '%s', '%s', '%s');" % (holiday[0], holiday[1], holiday[2], holiday[3], holiday[4])
        execute(ins_holidays)

execute(create_t_classes)
execute(create_t_department)
execute(create_t_holidays)
execute(create_t_rooms)
execute(create_t_schoolyears)
execute(create_t_subjects)
execute(create_t_teacher)
#execute(create_t_substitutions)

"""
SECTION to fill in the data.
"""
loadClasses()
loadDepartments()
loadRooms()
loadSubjects()
loadTeacher()
loadSchoolyears()
loadHolidays()
#loadSubstitutions()

# close connection to database
conn.commit()
conn.close()
WebUntis_Session.close_session(session)