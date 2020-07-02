FROM ros
EXPOSE 8800-9000
RUN apt-get update
RUN apt-get install -y python3-pip
RUN apt-get install -y python3-rosbag