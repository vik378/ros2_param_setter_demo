FROM ros:foxy-ros-base

# install pip3 and python deps
# RUN apt update
# RUN apt install --assume-yes python3-pip

# clone ros package repo
ENV ROS2_WS  /home/ros2_ws
RUN mkdir -p ${ROS2_WS}/src/ros2_param_setter_demo
COPY ./ ${ROS2_WS}/src/ros2_param_setter_demo

# build repo
RUN cd ${ROS2_WS} \
    && . /opt/ros/foxy/setup.sh \
    && colcon build \
    && . ${ROS2_WS}/install/setup.sh

WORKDIR ${ROS2_WS}
RUN echo "source install/setup.bash" >> /opt/ros/foxy/setup.bash

CMD ros2 launch ros2_param_setter_demo demo.launch.py