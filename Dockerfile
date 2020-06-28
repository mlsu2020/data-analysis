FROM ros
EXPOSE 8800-9000
RUN apt-get update
RUN apt-get install python3-pip -y