#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def callback(data):
	rospy.loginfo(data)

def listener():
	rospy.init_node('listener_test', anonymous=True)
	rospy.Subscriber('sender', String, callback=callback)
	rospy.spin()

if __name__=='__main__':
	listener()
