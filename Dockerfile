FROM resin/rpi-raspbian:stretch
MAINTAINER yamaryoxxxx@gmail.com

# initialization
RUN apt-get update

# install python
RUN apt-get install -y python net-tools

# import script
COPY mail-my-ip.py .

# variables
ENV SEND_FROM sender@gmail.com
ENV SEND_PASSWORD password-of-sender
ENV SEND_TO someone@somedomain.com
ENV WAIT 10

# entry point
CMD python mail-my-ip.py --sendfrom $SEND_FROM --password $SEND_PASSWORD --sendto $SEND_TO --wait $WAIT
