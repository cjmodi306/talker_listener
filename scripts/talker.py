#!/usr/bin/env python

import rospy
from std_msgs.msg import String


def talker():
	i = 1
	rospy.init_node("talker_test", anonymous=True)
	pub = rospy.Publisher('sender', String, queue_size=10)
	rate = rospy.Rate(1)
	while not rospy.is_shutdown():
		msg = "Hello World" + str(i)
		rospy.loginfo(msg)
		pub.publish(msg)
		i+=1
		rate.sleep()

if __name__ == '__main__':
	talker()
