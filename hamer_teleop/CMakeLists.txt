cmake_minimum_required(VERSION 2.8.3)
project(hamer_teleop)

## Find catkin macros and libraries
find_package(catkin REQUIRED COMPONENTS rospy roscpp geometry_msgs)

include_directories(${catkin_INCLUDE_DIRS})

catkin_package(
  INCLUDE_DIRS
  CATKIN_DEPENDS rospy roscpp geometry_msgs
  DEPENDS
)

#############
## Install ##
#############

## Mark executable scripts (Python etc.) for installation
install(PROGRAMS
  scripts/hamer_keyboard
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)

## Mark all other useful stuff for installation
install(DIRECTORY launch
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)
