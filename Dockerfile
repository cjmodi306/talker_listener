FROM ros:noetic

SHELL["/bin/bash" ,""-c]
RUN apt-get update && apt-get isntall -y git

RUN source /opt/ros/noetic/setup.bash \
    && mkdir -p ~/catkin_ws/src \
    && cd ~/catkin_ws/src
    && git clone