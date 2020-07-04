cmake_minimum_required(VERSION 2.8.3)
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


install(DIRECTORY include/${PROJECT_NAME}/
  DESTINATION ${CATKIN_PACKAGE_INCLUDE_DESTINATION}
)

install(DIRECTORY bag config launch rviz
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)


