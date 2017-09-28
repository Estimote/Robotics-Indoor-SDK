#!/usr/bin/env python
import time
import sys
import rospy
print "[Robotics Indoor SDK] initializing ROS node.."
rospy.init_node('positioning', anonymous=True)
print "[Robotics Indoor SDK] ROS node started, initializing positioning system.."
# sys.path.append('lib/armv7l')
sys.path.append('lib/x86')
import robotics_indoor_sdk
    
while True:
    time.sleep(0.2)
