#!/usr/bin/env python

import rospy 
from geometry_msgs.msg import Pose

rospy.init_node('robot')
pub = rospy.Publisher('my_position', Pose, queue_size=1)
rate = rospy.Rate(1) # 1hz

while not rospy.is_shutdown():
    pub.publish(Pose())
    rate.sleep()