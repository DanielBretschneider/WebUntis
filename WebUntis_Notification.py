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

class notification:
    def __init__(self, email, password):
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
        ''' This must be removed '''
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
        """

        try:
            self.send_message(receivers, subject, content)
            print "Notification successfully sent %s {from: %s, to: %s}" % (EOL, sender, receivers)
        except:
            print "Error: unable to send email"

def change_occured():
    """

    :return: TRUE, if change in the WebUntis has occured; None if nothing happend;
    """
    substitutions = WebUntisData.getSubstitutions(WEBUNTIS_SESSION)
    num_substitutions = len(substitutions)
    for sub in substitutions:
        print(sub)

def create_receiver_list():
    """
    create_receiver_list(): creates a list, including all teachers who are concerned of the change
    """

# teacher email-addresses
teachers = WebUntisData.getTeacher(WEBUNTIS_SESSION)

# Sender Email-Adress
sender = secret.gmail_sender

# Receiver
receivers = ['dani.bretschneider@gmail.com']

# message content
message = ""

# End of line
EOL = "\n"

msg = notification(secret.gmail_sender, secret.gmail_passwd)
notification.send_notification(msg, receivers, "Test", "This is a test.")

# close WebUntis session
WebUntisData.logout()