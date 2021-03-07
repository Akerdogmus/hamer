cmake_minimum_required(VERSION 3.0.2)
project(hamer_bringup)
add_compile_options(-std=c++11)
find_package(catkin REQUIRED COMPONENTS
  actionlib
  geometry_msgs
  move_base_msgs
  nav_msgs
  roscpp
  rospy
  std_msgs
  tf
)

catkin_package(
)

