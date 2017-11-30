#!/usr/bin/env python
import time
import rospy
print "[Robotics Indoor SDK] initializing ROS node.."
rospy.init_node('positioning', anonymous=True)
print "[Robotics Indoor SDK] ROS node started, initializing positioning system.."

#import lib.x86.robotics_indoor_sdk
import lib.armv7l.robotics_indoor_sdk
    
while True:
    time.sleep(0.2)
