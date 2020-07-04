#!/usr/bin/env python
"""
Created on Thu Feb 20 11:38:00 2020

@author: AKE
"""

import rospy
import roslib

from geometry_msgs.msg import Twist

import sys, select, termios, tty

msg = """
Control Your Hamer Robot!
---------------------------
Moving around:
       w    
   a   s   d
       x    

"""

"""
DAHA SONRA EKLENECEK
t/g : increase/decrease max speeds by 10%
y/h : increase/decrease only linear speed by 10%
u/j : increase/decrease only angular speed by 10%
CTRL-C to quit
"""

moveBindings = {
        'w':(1,0),
        'a':(0,1),
        'd':(0,-1),
        'x':(-1,0)

    }

"""speedBindings={
        't':(1.1,1.1),
        'g':(.9,.9),
        'y':(1.1,1),
        'h':(.9,1),
        'u':(1,1.1),
        'j':(1,.9),
    }"""

def getKey():
    tty.setraw(sys.stdin.fileno())
    rlist, _, _ = select.select([sys.stdin], [], [], 0.1)
    if rlist:
        key = sys.stdin.read(1)
    else:
        key = ''
        
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
    return key

speed = 1.9
turn = 1.9

def vels(speed,turn):
    return "currently:\tspeed %s\tturn %s " % (speed,turn)

if __name__=="__main__":
    settings = termios.tcgetattr(sys.stdin)

    rospy.init_node('hamer_teleop')
    pub = rospy.Publisher('/hamer/cmd_vel', Twist, queue_size = 5)

    x = 0
    th = 0
    status = 0
    count = 0
    acc = 0.1
    target_speed = 0
    target_turn = 0
    control_speed = 0
    control_turn = 0
    try:
        print(msg)
        print(vels(speed,turn))
        while(1):
            key = getKey()
            if key in moveBindings.keys():
                x = moveBindings[key][0]
                th = moveBindings[key][1]
                count = 0
            elif key == 's' :
                x = 0
                th = 0
                control_speed = 0
                control_turn = 0
            else:
                count = count + 1
                if count > 4:
                    x = 0
                    th = 0
                if (key == '\x03'):
                    break
            """elif key in speedBindings.keys():
                speed = speed * speedBindings[key][0]
                turn = turn * speedBindings[key][1]
                count = 0

                print(vels(speed,turn))
                if (status == 14):
                    print(msg)
                status = (status + 1) % 15"""
            target_speed = speed * x
            target_turn = turn * th

            if target_speed > control_speed:
                control_speed = min( target_speed, control_speed + 0.1 )
            elif target_speed < control_speed:
                control_speed = max( target_speed, control_speed - 0.1 )
            else:
                control_speed = target_speed

            if target_turn > control_turn:
                control_turn = min( target_turn, control_turn + 0.1 )
            elif target_turn < control_turn:
                control_turn = max( target_turn, control_turn - 0.1 )
            else:
                control_turn = target_turn

            twist = Twist()
            twist.linear.x = control_speed; twist.linear.y = 0; twist.linear.z = 0
            twist.angular.x = 0; twist.angular.y = 0; twist.angular.z = control_turn
            pub.publish(twist)

            #print("loop: {0}".format(count))
            #print("target: vx: {0}, wz: {1}".format(target_speed, target_turn))
            #print("publihsed: vx: {0}, wz: {1}".format(twist.linear.x, twist.angular.z))

    except Exception as e:
        print(e)

    finally:
        twist = Twist()
        twist.linear.x = 0; twist.linear.y = 0; twist.linear.z = 0
        twist.angular.x = 0; twist.angular.y = 0; twist.angular.z = 0
        pub.publish(twist)

        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
