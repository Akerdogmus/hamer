# Halikarnas Modular Education Robot (HAMER) - Version 1.1.0
HAMER is a robotic project that is being developed for robotic education. This repository contains ROS Melodic compatible robot packages of HAMER robot.
This metapackage includes the following subpackages.

https://github.com/Akerdogmus/hamer/blob/master/hamer.png?raw=true

- hamer_bringup: It is a subpackage containing hardware control of HAMER robot.
- hamer_description: It is the subpackage containing urdf files of the HAMER robot.
- hamer_navigation: It is the subpackage containing the navigation package files of the HAMER robot.
- hamer_simulation: It is a sub-package containing the package and launch files required for the simulation of the HAMER robot.
- hamer_slam: It is a sub-package containing the package and launch files required for mapping of the HAMER robot.
- hamer_teleop: It is a sub-package containing the codes required to control the HAMER robot from the keyboard in a simulated or hardware environment.

For HAMER_mini model : https://github.com/Akerdogmus/HAMER_mini

Rviz Launching:

    $ roslaunch hamer_simulation hamer_rviz.launch
    
Gazebo Launching:

    $ roslaunch hamer_simulation hamer_gazebo.launch
    or
    $ roslaunch hamer_simulation hamer_gazebo_emptyworld.launch
    or
    $ roslaunch hamer_simulation hamer_gazebo_maze.launch

SLAM Launching:

    $ roslaunch hamer_slam hamer_slam.launch
    
Teleop Launching:

    $ rosrun hamer_teleop hamer_teleop.py

Navigation Launching (Added v1.1):

    $ roslaunch hamer_navigation hamer_navigation.launch
    $ rosrun rviz rviz (for seeing navigation components)
 
NOTE: Before running keyboard code, run on terminal this codes:
        
        $ cd ~/hamer_teleop/scripts
        $ chmod +x hamer_teleop.py
    
------------------------------------------------------------------------------
Requirements:
--------------

- In order for the sensors to work properly, "gazebo_ros_pkgs" files must be downloaded to your workspace.

        $ git clone https://github.com/ros-simulation/gazebo_ros_pkgs.git -b melodic-devel
        
- In order for the SLAM to work, "slam_gmapping" package must be downloaded to your workspace.
    
        $ git clone https://github.com/ros-perception/slam_gmapping.git -b melodic-devel
        
- In order for the "joint_state_publisher" to work, "joint_state_publisher_gui" package must be downloaded to your computer.

        $ sudo apt update
        $ sudo apt install ros-melodic-joint-state-publisher-gui
        
---------------------------------------------------------------------------------
Changelog:
----------
Update v1.0 - 02.08.20
------------------------
- First version

Update v1.1 - 21.08.20
------------------------
- Added Gazebo Sonar Plugins (Now Sonar Sensors available)
- Added hamer_navigation subpackage (Now navigation tools and 2d nav goal available)
- Added new Gazebo maps and launch files

---------------------------------------------------------------------------------
Extras:
--------
- If you want to control the robot with the help of an interface, not a terminal, you can install Robotic Controller Interface in your workspace.

      $ git clone https://github.com/Akerdogmus/Robotic_Controller_Interface 
      
----------------------------------------------------------------------------------

Maintainer
--------------
- Alim Kerem Erdoğmuş - https://www.linkedin.com/in/alim-kerem-erdogmus/

Contributors
------------
- Enes YAZ - Navigation Subpackage Designer - https://www.linkedin.com/in/enes-yaz/
- Harun ÇOŞKUN - HAMER Robot Model Designer - https://www.linkedin.com/in/harun-%C3%A7o%C5%9Fkun-91a579159/
- Berkay YAŞAR - Map Designer - https://www.linkedin.com/in/efecan-berkay-yasar/
- Samet AYDOĞAN
