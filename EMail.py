#! /usr/bin/env python3
import datetime
import pprint
import sys
import subprocess
import os
import os.path

import webuntis

import secret

SENDMAIL = True

CACHEDIR = "./cache/"
LOGDIR = "./log/"

## http://stackoverflow.com/questions/10147455/trying-to-send-email-gmail-as-mail-provider-using-python
import smtplib
class Gmail(object):
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

    def send_message(self, toemail, subject, body):
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
            toemail,
            headers + "\r\n\r\n" + body)

try:
  lehrername = sys.argv[1]
except IndexError:
  lehrername = "HOR"

s = webuntis.Session(
    server='https://urania.webuntis.com',
    username= secret.untis_username,
    password= secret.untis_passwd,
    school='htl3r',
    useragent='WebUntis Test'
)

try:
  s.login()
except Exception as ce:
  print("Login failed:", ce)
  sys.exit(1)

start = datetime.date.today()
end = start + datetime.timedelta(days=14)

lehrer = s.teachers().filter(name=lehrername)[0]
table = s.timetable(teacher=lehrer, start=start, end=end).to_table()

EOL = "\n"

res = ""
res += "teacher: " + lehrername + EOL
res += "start  : " + str(start) + EOL
res += "end    : " + str(end) + EOL

foundsomething = False

for time, row in table:
   timetext = '{}'.format(time.strftime('%H:%M'))
   for date, cell in row:
      for period in cell:
        if period.code:
          klassen = ', '.join(cls.name for cls in period.klassen)
          gegst = ', '.join(su.name for su in period.subjects)
          cachefile = CACHEDIR + "-".join((lehrername,str(date),str(timetext),klassen,gegst))
          logfile = LOGDIR + "-".join((lehrername,str(date),str(timetext),klassen,gegst))

          if not os.path.exists(cachefile):
            foundsomething = True
            with open(cachefile, "w") as f:
              f.write("")
            with open(logfile, "w") as f:
              f.write("-".join((lehrername,str(date),str(timetext),klassen,gegst)))
  
            res += str(date) + " " + str(timetext) +  ": "
            res += gegst + " / "
            res += klassen + " / "
            res += period.code + EOL

if foundsomething:
  print(res)
  if SENDMAIL:
    print ("Mail to ", lehrername)
    gm = Gmail(secret.gmail_sender, secret.gmail_passwd)
    gm.send_message(lehrername+"@htl.rennweg.at", "Webuntis Changes", res)
    gm.send_message(secret.gmail_sender, "Webuntis Changes", res)
    gm.send_message("hor@htl.rennweg.at", "Webuntis Changes - Kopie", res)

s.logout()