cmake_minimum_required(VERSION 3.0.2)
project(hamer_slam)

find_package(catkin REQUIRED COMPONENTS
  roscpp
  sensor_msgs
)

catkin_package(
  #INCLUDE_DIRS include
  CATKIN_DEPENDS roscpp sensor_msgs  
)

include_directories(
  include
  ${catkin_INCLUDE_DIRS}
)

install(DIRECTORY bag launch
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)


