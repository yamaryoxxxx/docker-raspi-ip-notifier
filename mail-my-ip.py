import argparse
import smtplib
from email.mime.text import MIMEText
import commands

# parse args
parser = argparse.ArgumentParser(description='Send private IP info via email.')
parser.add_argument('--sendto', type=str, help='TO addr', required=True)
parser.add_argument('--sendfrom', type=str, help='FROM Gmail addr', required=True)
parser.add_argument('--password', type=str, help='Password for FROM addr', required=True)
args = parser.parse_args()

# get info
ifconfig = commands.getstatusoutput('ifconfig')[1]
hostname = commands.getstatusoutput('hostname')[1]

print ifconfig
print hostname
# title and body
title = 'RasPi network info: %s' % hostname
body = ifconfig

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
