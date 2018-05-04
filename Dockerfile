FROM resin/rpi-raspbian:stretch
MAINTAINER yamaryoxxxx@gmail.com

# initialization
RUN apt-get update

# install python
RUN apt-get install -y python2.7

# import script
COPY mail-my-ip.py .

# entry point
CMD python mail-my-ip.py
