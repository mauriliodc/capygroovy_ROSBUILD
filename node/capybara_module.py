#Math stuff
from math import cos
from math import sin

#Rodent Stuff
from capybara_parser import CapybaraParser
from capybara_utils import add_nulls


#ROS stuff
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Quaternion

#Custom Messages
from capygroovy.msg import Ticks

import rospy

class Capybara_robot:

    #Calibration parameters
    _leftTicks = 0
    _righTicks = 0
    _baseline = 0
    _maxLinearSpeed = 0
    _maxAngularSpeed = 0

    #Pose
    _x = 0
    _y = 0
    _theta = 0

    #Velocity
    _linearSpeed = 0
    _angularSpeed = 0

    #Serial
    _serialPort = 0

    #Parser
    _capybaraParser = None

    #Odometry Publisher
    _odometryPublisher=None
    _TFPublisher=None
    
    #TicksPublisher
    _TICKPub=None
    #Name
    _robotName=0
    
    def __init__(self, leftTicks, RightTicks, Baseline, LinearSpeed, AngularSpeed, serialPort,odom,tf,tickPub,robotName):
        self._leftTicks = leftTicks
        self._rightTicks = RightTicks
        self._baseline = Baseline
        self._maxLinearSpeed = LinearSpeed
        self._maxAngularSpeed = AngularSpeed

        self._x = 0
        self._y = 0
        self._theta = 0

        self._robotName=robotName

        self._odometryPublisher=odom
        self._TFPublisher=tf
        self._TICKPub=tickPub
        print "Capybara init"
        self._serialPort = serialPort
        print "Serial init"
        self._capybaraParser = CapybaraParser(self._serialPort, self)
        
        print "Capybara ready"

    #Odometry setters
    #-----------------------------------------------------------------------------------------------------------
    def resetOdometry(self):
        self._x = 0
        self._y = 0
        self._theta = 0

    def setOdometry(self, x, y, theta):
        self._x = x
        self._y = y
        self._theta = theta
    #-----------------------------------------------------------------------------------------------------------


    def closeSerialConnection(self):
        self._capybaraParser.closeAll()

    #Odometry computation
    #-----------------------------------------------------------------------------------------------------------
    def computeOdometryFromTicks(self, tr, tl):
        #Publishing ticks BRAND NEW FEATURE!!!!!
        ticks = Ticks()
	ticks.header.stamp =rospy.get_rostime()
	ticks.leftTick=tl
	ticks.rightTick=tr
        self._TICKPub.publish(ticks)
        #----------------------------------------
        #Testing this
        #----------------------------------------
        
        dr = self._rightTicks * tr
        dl = self._leftTicks * (tl)
        R = (dl + dr) / (2)
        t = (dr-dl) / (self._baseline)
        self. _theta += t
        x = R * cos(self._theta)
        y = R * sin(self._theta)
        self. _x += x
        self. _y += y
        self.publishOdometry()

    def publishOdometry(self):
        quaternion = Quaternion()
        quaternion.x = 0.0
        quaternion.y = 0.0
        quaternion.z = sin( self. _theta / 2.0)
        quaternion.w = cos( self. _theta / 2.0)
        self._TFPublisher.sendTransform((self. _x,self. _y, 0), (quaternion.x, quaternion.y, quaternion.z, quaternion.w),rospy.Time.now(),
        "/"+self._robotName+"/"+"base_footprint",
        "/"+self._robotName+"/"+"odom")

        odom = Odometry()
        odom.header.frame_id = "/"+self._robotName+"/"+"odom"
        odom.child_frame_id = "/"+self._robotName+"/"+"base_footprint"
        odom.header.stamp = rospy.Time.now()
        odom.pose.pose.position.x = self. _x
        odom.pose.pose.position.y = self. _y
        odom.pose.pose.position.z = 0
        odom.pose.pose.orientation = quaternion
        odom.twist.twist.linear.x = 0
        odom.twist.twist.linear.y = 0
        odom.twist.twist.angular.z = 0
        self._odometryPublisher.publish(odom)

    def serialHandler(self, sensedLeftTicks, sensedRightTicks):
        self.computeOdometryFromTicks(-sensedLeftTicks, sensedRightTicks)
        #print "X: "+str(self. _x)+" Y: "+str(self. _y)+" T: "+str(self. _theta)

    def kill(self):
            self._capybaraParser.closeAll()
            
    #Velocity setters
    #-----------------------------------------------------------------------------------------------------------
    def setSpeed(self, linear, angular):
        self._linearSpeed = linear * self._maxLinearSpeed
        self._angularSpeed = angular * self._maxAngularSpeed
        leftSpeed = self._linearSpeed
        rightSpeed = self._angularSpeed
        
        rval = int(leftSpeed + rightSpeed)
        lval = int(leftSpeed-rightSpeed)

        rdir = "0"
        ldir = "1"
        if rval < 0:
            rdir = "1"
            rval = abs(rval)
        if lval < 0:
            ldir = "0"
            lval = abs(lval)
        lval = add_nulls(int(lval),2)
        rval = add_nulls(int(rval),2)
        self._capybaraParser.sendSpeedCommand(ldir,rdir,lval,rval)
