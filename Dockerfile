From ubuntu:16.04
RUN apt-get update && apt-get install vim -y
RUN apt-get install python3 -y python3-pip -y
RUN pip3 install requests
RUN mkdir /home/bobot
WORKDIR /home/bobot
