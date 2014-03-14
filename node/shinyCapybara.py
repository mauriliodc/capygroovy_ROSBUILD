#!/usr/bin/env python

#ROS imports
import rospy
import roslib
roslib.load_manifest('capygroovy')
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Twist
from capygroovy.msg import Ticks
import tf
#--------------------------------------------------------------

#System imports
import sys
import signal
#--------------------------------------------------------------

#Rodent stuff
from capybara_module import Capybara_robot

#REAL CODE
def signal_handler(signal, frame):
    print 'Killing the capys'
    global capy
    capy.kill()
    print 'Killed'
    sys.exit(0)

def SerialVelocityCommandSender(data):
    global capy
    capy.setSpeed(-data.linear.x, data.angular.z)


def MainLoop():
    rospy.Subscriber("cmd_vel", Twist, SerialVelocityCommandSender)
    rospy.spin()

if __name__ == '__main__':

    signal.signal(signal.SIGINT, signal_handler)
    
    rospy.init_node('capybara_control', anonymous=True)
    rospy.myargv(argv=sys.argv)


    print "\nAvailable parameters:\n"
    print "_calibTickLeft"
    print "_calibTickRight"
    print "_calibBaseline"
    print "_serialPort"
    print "_maxLSpeed"
    print "_maxASpeed"

    
    odometryPublisher = rospy.Publisher('odom', Odometry)
    tfPublisher = tf.TransformBroadcaster()
    tickPublisher = rospy.Publisher('ticks', Ticks)
    
    #calibTickLeft = rospy.get_param('~calibTickLeft', 1.40e-05)
    #calibTickRight = rospy.get_param('~calibTickRight', 1.40e-05)
    calibTickLeft = rospy.get_param('~calibTickLeft', 6.72e-05)
    calibTickRight = rospy.get_param('~calibTickRight', 6.72e-05)
    calibBaseline = rospy.get_param('~calibBaseline', 0.345)
    serialPort = rospy.get_param('~serialPort', '/dev/ttyUSB0')
    maxLSpeed =  rospy.get_param('~maxLSpeed',60)
    maxASpeed =  rospy.get_param('~maxASpeed',60)
    robotName =  rospy.get_param('~robotName',"bigRodent")
    
    capy = Capybara_robot(  calibTickLeft,
                                               calibTickRight,
                                               calibBaseline,
                                               maxLSpeed,
                                               maxASpeed,
                                               serialPort,
                                               odometryPublisher,
                                               tfPublisher,
                                               tickPublisher,
                                               robotName)
    MainLoop()
    
    
