cmake_minimum_required(VERSION 3.0.2)

project(hamer_description)
add_compile_options(-std=c++11)

find_package(catkin REQUIRED COMPONENTS
  urdf
  xacro
)

catkin_package(
  CATKIN_DEPENDS urdf xacro
)

find_package(roslaunch)

foreach(dir config launch meshes rviz urdf)
	install(DIRECTORY ${dir}/
		DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/${dir})
endforeach(dir)
