#! /usr/bin/env python3

"""
__author__ = "Daniel Bretschneider"
__version__ = "1.0.1"
__email__ = "dani.bretschneider@gmail.com"
__status__ = "(More or less) Finished."
"""

import smtplib
import secret
import WebUntisData

# WebUntis Session opening
WEBUNTIS_SESSION = WebUntisData.getSession()

# teacher email-addresses
teachers = WebUntisData.getTeacher(WEBUNTIS_SESSION)

# Sender Email-Adress
sender = secret.gmail_sender

# Receiver
receivers = ['dani.bretschneider@gmail.com']
copyReceivers = ['hor@htl.rennweg.at', 'bre@htl.rennweg.at']

# message content
message = ""

# email suffix
suffix = "@htl.rennweg.at"

# file which saves all already sent change-information
LOGFILE = "log/WEBUNTIS_LOG.log"

# End of line
EOL = "\n"

class notification:
    def __init__(self, email, password):
        """
        __init__(): classic constructor.

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
            self.send_message(receivers, subject, content)
            print "Notification successfully sent %s {from: %s, to: %s}" % (EOL, sender, receivers)
        except:
            print "Error: unable to send email"

def log(receivers, content):
    """
    log(): saves already sent info-mails.

    :param receivers:
    :param content:
    :return:
    """
    with open(LOGFILE, "w") as logfile:
        logfile.write("Mail sent to {REC} {newline} with content:{newline}{CONT}".format(REC=receivers, newline=EOL, CONT=content))

def check_for_changes():
    """
    change_occured: responsible for the recognition of webuntis changes. TODO: AGAIN!

    :return: TRUE, if change in the WebUntis has occured; None if nothing happend;
    """



def create_receiver_list():
    """
    create_receiver_list(): creates a list, including all teachers who are concerned of the change
    :return:
    """

def notificate():
    """
    notificate(): method to send out the change-information.
    :return:
    """
    msg = notification(secret.gmail_sender, secret.gmail_passwd)
    notification.send_notification(msg, receivers, "Automatic WebUntis Change Notification", "This is a test.")
#   notification.send_notification(msg, copyReceivers, "Test", "This is a test.")

# close WebUntis session
WebUntisData.logout()