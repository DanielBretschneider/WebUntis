#! /usr/bin/env python3
# coding: utf8

"""
__author__ = "Daniel Bretschneider"
__version__ = "1.0.1"
__email__ = "dani.bretschneider@gmail.com"
__status__ = "(More or less) Finished."
"""

#
# This program is responsible for the automatic WebUnits Change Notifications.
#

import smtplib
import secret
import WebUntisData
import logging
import os
from datetime import datetime

# WebUntis Session opening
WEBUNTIS_SESSION = WebUntisData.getSession()

# teacher email-addresses
teachers = WebUntisData.getTeacher_shortname()

# Sender Email-Adress
sender = secret.gmail_sender

# Receiver
receivers = ['dani.bretschneider@gmail.com',  'hor@htl.rennweg.at']
#copyReceivers = ['hor@htl.rennweg.at', 'bre@htl.rennweg.at']

# message content
message = ""

# email suffix
suffix = "@htl.rennweg.at"

# logging
LOGFILE = ".log/WEBUNTIS_LOG.LOG"
logging.basicConfig(filename=LOGFILE, level=logging.INFO)

# Caching
CACHEFILE = ".cache/CACHEFILE.CACHE"

# End of line
EOL = "\n"

# Change occured
CHANG_OCCURED = False

class notification:
    def __init__(self, email, password):
        """
        __init__(): classic constructor

        :param email:
        :param password:
        :return:
        """
        self.email = email
        self.password = password
        self.server = 'smtp.gmail.com'
        self.port = 587
        session = smtplib.SMTP(self.server, self.port)
        session.ehlo()
        session.starttls()
        session.ehlo
        session.login(self.email, self.password)
        self.session = session
        logging.info(str(datetime.now()) + " :: Initialized SMTP Server, Logon successful.")

    def send_message(self, receiver, subject, body):
        """
        send_message: sends the email.

        :param receiver: list of teachers
        :param subject: WebUntis Change-Notification
        :param body: date of change, class and classroom, kind of change (substitution, cancel, shift)
        :return: None.
        """
        headers = [
            "From: " + self.email,
            "Subject: " + subject,
            "To: " + self.email,
            "MIME-Version: 1.0",
           "Content-Type: text/plain"]
        headers = "\r\n".join(headers)
        self.session.sendmail(
            self.email,
            receiver,
            headers + "\r\n\r\n" + body)

    def send_notification(self, receiver, subject, content):
        """
        send_notification: Sends the message to the concerning teachers.

        :return:
        """

        try:
            self.send_message(receiver, subject, content)
            logging.info(str(datetime.now()) + " :: Notification successfully sent %s {from: %s, to: %s}" % (EOL, sender, receivers))
            print "Notification successfully ssent %s {from: %s, to: %s}" % (EOL, sender, receivers)
        except:
            logging.warn(str(datetime.now()) + " :: Error occurred: Unable to send email")
            print "Error: unable to send email"

def check_for_changes():
    """
    change_occured: responsible for the recognition of webuntis changes.

    :return: TRUE, if change in the WebUntis has occured; None if nothing happend;
    """
    # Normally variable 'teachers' will be used instead of 'teacherlist' - just for testing.
    teacherlist = ['HOR']

    for teacher in teacherlist:
        substitutions = WebUntisData.getSubstitutionForSpecificTeacher(teacher)
        numSubstitutions = len(substitutions)
        if numSubstitutions == 0:
            CHANG_OCCURED = False
        elif numSubstitutions > 0:
            CHANG_OCCURED = True
            message = WebUntisData.printSubstitutionForSpecificTeacher(teacher)
            notify(message)

def format_content(lst):
    """

    :return:
    """
    c=0
    lst = lst[4:]
    lst[-1]
    return lst

def cache(txt):
    """
    cache(): saves already sent information, to prevent redundant mails.
    :param txt: email-content; substitutions
    :return: nothing
    """
    entry = format_content(txt.split(EOL))

    if os.path.exists(CACHEFILE):
        with open(CACHEFILE, "a") as f:
            for line in entry:
                f.write(line+EOL)
                logging.info(str(datetime.now()) + " :: CACHED into ./cache/CACHEFILE.CACHE: %s%s%s" % (EOL, line, EOL))


def unified_subject_extension():
    """
    unified_subject_extension(): This method generates a unfied extension, which will be added to the original subject.
                                 Because many email clients tend to group emails with the same subject...
    :return: something unique
    """
    time = datetime.now()
    day = str(time.day)
    month = str(time.month)
    year = str(time.year)

    extension = "%s-%s-%s" % (day, month, year)

    return extension


def notify(msg):
    """
    notificate(): method to send out the change-information.
    :return:
    """
    # subejct
    subject = " TIME Change Notification - " + unified_subject_extension()

    # setup mail server
    mail = notification(secret.gmail_sender, secret.gmail_passwd)
    mail.send_notification(receivers, subject, msg)
#    cache(msg)
    print(msg)
#   notification.send_notification(msg, copyReceivers, subject+" (Copy)", msg)
    #print(msg)

check_for_changes()

# close WebUntis session
WebUntisData.logout()

# daily checks
# 07:50 / 08:30 / 10:05 / 14:00 / 18:00