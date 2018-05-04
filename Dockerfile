FROM resin/rpi-raspbian:stretch
MAINTAINER yamaryoxxxx@gmail.com

# initialization
RUN apt-get update

# import script
COPY mail-my-ip.py 

# install python
RUN apt-get install -y python2.7

# entry point
CMD python mail-my-ip.py
