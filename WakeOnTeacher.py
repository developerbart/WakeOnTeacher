#!/usr/local/bin/python3
from smtplib import SMTP

fromaddr = "John.Doe@Doe.com"
toaddr = "Jane.Doe@Doe.com"

header = "To:" + toaddr + "\n" + "From: " + fromaddr + "\n" + "Subject: Subject \n"

msg = header + '''\n Content \n
'''

server = SMTP("MAILSERVER.com",587)
server.starttls()
server.login("username","password")
server.sendmail(fromaddr, toaddr, msg)
server.quit()
