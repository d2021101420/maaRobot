# Trabalho de PCO112
# ROS2 e GAZEBO

<b>Robo com laser 360º</b>

<p>Mauricio Andre de Almeida</p>
<p>Mestrando em Ciência e Tecnologia da Computação</p>
<p>Universidade Federal de Itajubá</p>
<p>Matrícula 2021101420</p>

![demo.gif animation](resources/maa_robot2.gif)

INSTRUCOES
===========

Instalar ROS2 e GAZEBO

source /opt/ros/foxy/setup.bash

colcon build

. install/local_setup.bash

Abrir em um terminal:
source /opt/ros/foxy/setup.bash
ros2 launch warehouse_robot_controller_pkg controller_estimator.launch.py

Abrir em outro terminal:
source /opt/ros/foxy/setup.bash
ros2 launch maa_robot_spawner_pkg gazebo_world.launch.py

Fontes usadas neste trabalho:

<p>https://github.com/chapulina/dolly</p>
<p>https://docs.ros.org/en/foxy/Tutorials/Workspace/Creating-A-Workspace.html</p>
<p>https://automaticaddison.com/how-to-simulate-a-robot-using-gazebo-and-ros-2/</p>

