# Halikarnas Modular Education Robot (HAMER) - Version 1.3.1 &nbsp; ![](https://img.shields.io/github/forks/Akerdogmus/hamer?style=social) ![](https://img.shields.io/github/stars/Akerdogmus/hamer?style=social) ![](https://img.shields.io/github/watchers/Akerdogmus/hamer?style=social) <br>

![](https://img.shields.io/github/repo-size/Akerdogmus/hamer) ![](https://img.shields.io/github/license/Akerdogmus/hamer?color=red) ![](https://img.shields.io/github/downloads/Akerdogmus/hamer/total) ![](https://img.shields.io/github/last-commit/Akerdogmus/hamer) ![](https://img.shields.io/github/contributors/Akerdogmus/hamer)
HAMER is a robotic project that is being developed for robotic education. This repository contains ROS Melodic (branch: melodic-devel) and ROS Noetic (branch: noeitc-devel) compatible robot packages of HAMER robot.
This metapackage includes the following subpackages.

![Image of HAMER](https://github.com/Akerdogmus/hamer/blob/noetic-devel/hamer.png?raw=true)

- hamer_bringup: It is a subpackage containing hardware control of HAMER robot.
- hamer_description: It is the subpackage containing urdf files of the HAMER robot.
- hamer_navigation: It is the subpackage containing the navigation package files of the HAMER robot.
- hamer_simulation: It is a sub-package containing the package and launch files required for the simulation of the HAMER robot.
- hamer_slam: It is a sub-package containing the package and launch files required for mapping of the HAMER robot.
- hamer_teleop: It is a sub-package containing the codes required to control the HAMER robot from the keyboard in a simulated or hardware environment.

For HAMER_mini model : https://github.com/Akerdogmus/HAMER_mini

HAMER Installation:
-------------------
ROS Melodic version:

```bash
git clone https://github.com/Akerdogmus/hamer -b melodic-devel
```

ROS Noetic version:

```bash
git clone https://github.com/Akerdogmus/hamer -b noetic-devel
```

Some HAMER ROS Commands:
---------------------
Rviz Launching:

```bash
roslaunch hamer_simulation hamer_rviz.launch
```

Solo-Rviz Launching (v1.3 Update):

```bash
roslaunch hamer_simulation hamer_rviz_standalone.launch
```

Gazebo Launching:

```bash
roslaunch hamer_simulation hamer_gazebo.launch
```
or

```bash
roslaunch hamer_simulation hamer_gazebo_emptyworld.launch
```
or

```bash    
roslaunch hamer_simulation hamer_gazebo_maze.launch
```

SLAM Launching:

```bash
roslaunch hamer_slam hamer_slam.launch
```

Teleop Launching:

```bash
rosrun hamer_teleop hamer_teleop.py
```

Navigation Launching (Added v1.1):

```bash
roslaunch hamer_navigation hamer_navigation.launch
```

![Image of HAMER_2](https://github.com/Akerdogmus/hamer/blob/noetic-devel/hamer_2.png?raw=true)
 
NOTE: Before running keyboard code, run on terminal this codes:

```bash        
cd ~/hamer_teleop/scripts && chmod +x hamer_teleop.py
```
------------------------------------------------------------------------------
Requirements:
--------------

- In order for the sensors to work properly, "gazebo_ros_pkgs" files must be downloaded to your workspace.

```bash
git clone https://github.com/ros-simulation/gazebo_ros_pkgs.git -b noetic-devel
```

- In order for the SLAM to work, "slam_gmapping" package must be downloaded to your workspace.

```bash    
git clone https://github.com/ros-perception/slam_gmapping.git -b noetic-devel
```

- In order for the "joint_state_publisher" to work, "joint_state_publisher_gui" package must be downloaded to your computer.

```bash
sudo apt update && sudo apt install ros-melodic-joint-state-publisher-gui
```

- In order for the navigation package to work, "follow_waypoint" package must be downloaded to your workspace.
(Waypoints package added and the default goal tolerance increased to 0.3 from 0.0 in phyton script to ease robot's movement.)

```bash
git clone https://github.com/danielsnider/follow_waypoints
```

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

Update v1.2 - 08.09.20
----------------------
"hamer_navigation" Package Changes:
- base_local_planner parameters changed.
- costmap_common_parameters new parameters added and existing upgraded.
- Added new parameters for global_costmap and local costmap.
- costmap_converter, teb_local_planner in param folder and cfg folder in navigation package removed.
- navigation launch file: The param teb_local_planner is removed. Instead, TrajectoryPlannerRos used.
- Rviz starting added to launch file.

Update v1.3 - 07.03.21
----------------------
- HAMER is now ROS Noetic compatible.
- "hamer_rviz_standalone.launch" file added (For using HAMER Rviz without Gazebo working)

"hamer_teleop" Package Changes: 
- for teleop operation Launch file added so only launch file is enough to use keyboard.

Update v1.3.1 - 16.03.21
------------------------
- Some bug and file fixes.
---------------------------------------------------------------------------------
Extras:
--------
- If you want to control the robot with the help of an interface, not a terminal, you can install Robotic Controller Interface in your workspace.

```bash
git clone https://github.com/Akerdogmus/Robotic_Controller_Interface 
```

- HAMER Robots YouTube Channel: https://www.youtube.com/channel/UCJIAVXEoZ3Qzcn72Dd_9upg/featured?disable_polymer=1
      
----------------------------------------------------------------------------------

Maintainer
--------------
- Alim Kerem Erdoğmuş - https://www.linkedin.com/in/alim-kerem-erdogmus/

Contributors
------------
- Enes YAZ - Navigation Subpackage Designer - https://www.linkedin.com/in/enes-yaz/
- Harun ÇOŞKUN - HAMER Robot Model Designer - https://www.linkedin.com/in/harun-%C3%A7o%C5%9Fkun-91a579159/
- Berkay YAŞAR -Test Maps Designer - https://www.linkedin.com/in/efecan-berkay-yasar/
- Samet AYDOĞAN - http://www.linkedin.com/in/samet-aydogan
- Muhammed KOCAOĞLU - Navigation Subpackage Designer - https://www.linkedin.com/in/muhammed-kocaoğlu-2b661b178/
- Fatih VATANSEVER - Experiments and Interface Designer - https://www.linkedin.com/in/fatihvatansever/
- Yağız UMUR -  Experiments and Interface Designer - https://www.linkedin.com/in/yagizumur/
- Berkay YARIŞ - Experiments and Interface Designer - https://www.linkedin.com/in/berkayyaris/

Supervisor
------------
- Muhammed Oğuz TAŞ - https://www.linkedin.com/in/moguztas/
