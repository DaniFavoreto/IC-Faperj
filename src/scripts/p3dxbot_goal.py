#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import math
import time
from std_srvs.srv import Empty
from nav_msgs.msg import Odometry

x=0
y=0
yaw=0

def poseCallback(odom_data):
    global x
    global y, yaw
    pose_message = odom_data.pose.pose
    print( pose_message.position)
    x= pose_message.position.x
    y= pose_message.position.y
    yaw = pose_message.orientation.z

    #print "pose callback"
    #print ('x = {}'.format(pose_message.x)) #new in python 3
    #print ('y = %f' %pose_message.y) #used in python 2
    #print ('yaw = {}'.format(pose_message.theta)) #new in python 3


def move(speed, distance, is_forward):
        #declare a Twist message to send velocity commands
        velocity_message = Twist()
        #get current location 
        global x, y
        x0=x
        y0=y

        if (is_forward):
            velocity_message.linear.x =abs(speed)
        else:
        	velocity_message.linear.x =-abs(speed)

        distance_moved = 0.0
        loop_rate = rospy.Rate(10) # we publish the velocity at 10 Hz (10 times a second)    
        cmd_vel_topic='/p3dx/cmd_vel'
        velocity_publisher = rospy.Publisher(cmd_vel_topic, Twist, queue_size=10)

        while True :
                rospy.loginfo("p3dxbot moves forwards")
                velocity_publisher.publish(velocity_message)

                loop_rate.sleep()
                
                #rospy.Duration(1.0)
                
                distance_moved = abs(0.5 * math.sqrt(((x-x0) ** 2) + ((y-y0) ** 2)))
                print  distance_moved               
                if  not (distance_moved<distance):
                    rospy.loginfo("reached")
                    break
        
        #finally, stop the robot when the distance is moved
        velocity_message.linear.x =0
        velocity_publisher.publish(velocity_message)
    
def rotate (angular_speed_degree, relative_angle_degree, clockwise):
    
    global yaw
    velocity_message = Twist()
    velocity_message.linear.x=0
    velocity_message.linear.y=0
    velocity_message.linear.z=0
    velocity_message.angular.x=0
    velocity_message.angular.y=0
    velocity_message.angular.z=0

    #get current location 
    theta0=yaw
    angular_speed=math.radians(abs(angular_speed_degree))

    if (clockwise):
        velocity_message.angular.z =-abs(angular_speed)
    else:
        velocity_message.angular.z =abs(angular_speed)

    angle_moved = 0.0
    loop_rate = rospy.Rate(10) # we publish the velocity at 10 Hz (10 times a second)    
    cmd_vel_topic='/p3dx/cmd_vel'
    velocity_publisher = rospy.Publisher(cmd_vel_topic, Twist, queue_size=10)

    t0 = rospy.Time.now().to_sec()

    while True :
        rospy.loginfo("Turtlesim rotates")
        velocity_publisher.publish(velocity_message)

        t1 = rospy.Time.now().to_sec()
        current_angle_degree = (t1-t0)*angular_speed_degree
        loop_rate.sleep()


                       
        if  (current_angle_degree>relative_angle_degree):
            rospy.loginfo("reached")
            break

    #finally, stop the robot when the distance is moved
    velocity_message.angular.z =0
    velocity_publisher.publish(velocity_message)

if __name__ == '__main__':
    try:
        
        rospy.init_node('turtlesim_motion_pose', anonymous=True)

        #declare velocity publisher
        cmd_vel_topic='/p3dx/cmd_vel'
        velocity_publisher = rospy.Publisher(cmd_vel_topic, Twist, queue_size=10)
        
        position_topic = "/p3dx/odom"
        pose_subscriber = rospy.Subscriber(position_topic, Odometry, poseCallback) 
        time.sleep(2)

        move(0.2, 2, True )
        rotate(15, 90, True)
        rotate(15, 90 + 40, False)
        move(0.2, 2, True)
        rotate(15, 90 + 40, True)
        rotate(15, 90, False)
        move(0.2, 3, True)
        rotate(15, 90 + 60, True)
        rotate(15, 60 + 50, False)
        move(0.2, 2, True)  
        rotate(15, 120, True)
        rotate(15,120, False)
        move(0.2, 2, True)
        rotate(15, 110 + 50, True)
        rotate(15,110 + 10, False)
        move(0.2, 2, True)
        rotate(15, 140, True)
        rotate(15, 140, False)
        move(0.2, 2, True)
        rotate(15, 140, True)
        rotate(15, 140, False)
        move(0.2, 2, True)
        rotate(15, 140, True)
        rotate(15, 140, False)
        move(0.2, 2, True)
        rotate(15, 140, True)
        rotate(15, 130, False)
        move(0.2, 2, True) 
        rotate(15, 140,True)
        rotate(15, 52, False)
        move(0.2, 2, True)
        rotate(15, 140, True)
        rotate(15, 140, False)
        move(0.2, 2, True)
        rotate(15, 140, True)
        rotate(15, 140, False)
        move(0.2, 2, True)
        rotate(15, 140, True)
        rotate(15, 140, False)
        move(0.2, 2, True)
        rotate(15, 140, True)
        rotate(15, 140, False)
        move(0.2, 2, True)
        
    
   
        #go_to_goal(1.0, 1.0)
        #setDesiredOrientation(math.radians(90))
       
    except rospy.ROSInterruptException:
        rospy.loginfo("node terminated.")
