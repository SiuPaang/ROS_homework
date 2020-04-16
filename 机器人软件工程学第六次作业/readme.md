# 此处为机器人软件工程学第六次作业
- 在机器人上添加了一个hobuyo激光雷达用作建图以及导航

$ roslaunch turtlebot_gazebo turtlebot_world.launch

$ roslaunch turtlebot_gazebo amcl_demo.launch map_file:=/home/usrname/map.yaml

$ roslaunch turtlebot_rviz_launchers view_navigation.launch

$ roslaunch robot_navigation say.launch

$ rosrun robot_navigation navigation.py

- robot_navigation为本功能包名字
- say.launch中的chat_recognizer.py在语音第四次作业功能包中
- 运行时地图存放在主文件夹
