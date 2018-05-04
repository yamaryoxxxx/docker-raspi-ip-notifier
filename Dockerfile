FROM resin/rpi-raspbian:stretch
MAINTAINER yamaryoxxxx@gmail.com

# initialization
RUN apt-get update

# install python
RUN apt-get install -y python

# import script
COPY mail-my-ip.py .

# variables
ENV SEND_FROM sender@gmail.com
ENV SEND_PASSWORD password-of-sender
ENV SEND_TO someone@somedomain.com

# entry point
CMD sleep 30 && python mail-my-ip.py --sendfrom $SEND_FROM --password $SEND_PASSWORD --sendto $SEND_TO
