import argparse
import smtplib
from email.mime.text import MIMEText
import commands
import time

# parse args
parser = argparse.ArgumentParser(description='Send private IP info via email.')
parser.add_argument('--sendto', type=str, help='TO addr', required=True)
parser.add_argument('--sendfrom', type=str, help='FROM Gmail addr', required=True)
parser.add_argument('--password', type=str, help='Password for FROM addr', required=True)
parser.add_argument('--wait', type=int, default=15, help='wait time before send email(sec)')
parser.add_argument('--host', type=str, help='hostname', required=True)
args = parser.parse_args()

# get info
time.sleep(args.wait)
info = commands.getstatusoutput('ifconfig')[0]

# title and body
title = 'RasPi network info: %s' % args.host
body = info

# send mail
smtpserver = smtplib.SMTP('smtp.gmail.com', 587)
smtpserver.ehlo()
smtpserver.starttls()
smtpserver.ehlo
smtpserver.login(args.sendfrom, args.password)
msg = MIMEText(body)
msg['Subject'] = title
msg['From'] = args.sendfrom
msg['To'] = args.sendto
smtpserver.sendmail(args.sendfrom, [args.sendto], msg.as_string())
smtpserver.quit()
