FROM ubuntu:16.04
MAINTAINER OOCRAN Project <info@oocran.dynu.com>

#Update
RUN apt-get update -y

#Install dependecies
RUN apt-get install python-pip -y
RUN apt-get install git -y

#Install OOCRAN
RUN git clone https://github.com/oocran/oocran.git && cd oocran && python setup.py install

EXPOSE 8000

CMD oocran start localhost:8000
