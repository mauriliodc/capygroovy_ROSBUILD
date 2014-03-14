#!/usr/bin/env python


import roslib
roslib.load_manifest('capygroovy')
import rospy
from capygroovy.msg import Ticks

rospy.init_node('tickPublisher', anonymous=True)
tickPublisher = rospy.Publisher('ticks', Ticks)

while 1==1:
	print "PUSH"
	ticks = Ticks()
	ticks.header.stamp =rospy.get_rostime()
	ticks.leftTick=60
	ticks.rightTick=90
	tickPublisher.publish(ticks)
