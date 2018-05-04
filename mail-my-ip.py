import argparse
import smtplib
from email.mime.text import MIMEText
import commands

# parse args
parser = argparse.ArgumentParser(description='Send private IP info via email.')
parser.add_argument('--to', type=str, help='TO addr', required=True)
parser.add_argument('--from', type=str, help='FROM Gmail addr', required=True)
parser.add_argument('--password', type=str, help='Password for FROM addr', required=True)
args = parser.parse_args()

# get info
ifconfig = commands.getstatusoutput('ifconfig')
hostname = commands.getstatusoutput('hostname')

# title and body
title = 'RasPi network info: %s' % hostname
body = ifconfig

# send mail
smtpserver = smtplib.SMTP('smtp.gmail.com', 587)
smtpserver.ehlo()
smtpserver.starttls()
smtpserver.ehlo
smtpserver.login(args.from, args.password)
msg = MIMEText(body)
msg['Subject'] = title
msg['From'] = args.from
msg['To'] = args.to
smtpserver.sendmail(args.from, [args.to], msg.as_string())
smtpserver.quit()
