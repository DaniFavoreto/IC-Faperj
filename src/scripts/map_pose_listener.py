#!/usr/bin/env python  
import rospy
import math
import tf
import geometry_msgs.msg
import turtlesim.srv
import csv
import time

if __name__ == '__main__':
    rospy.init_node('frame_a_frame_b_listener_node')

    listener = tf.TransformListener()
    rate = rospy.Rate(1.0)
    listener.waitForTransform('map', 'p3dx/odom', rospy.Time(), rospy.Duration(4.0))

    fieldnames = ["x_value", "y_value"]

    with open('map_data2.csv','w') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        csv_writer.writeheader()
    
    while not rospy.is_shutdown():
        try:
            (trans,rot) = listener.lookupTransform('map', 'p3dx/base_link', rospy.Time(0))
        except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
            continue

        with open('map_data2.csv','a') as csv_file:
            csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            info = {
                "x_value": trans[0],
                "y_value": trans[1],

            }
            time.sleep(0.2)
        
            csv_writer.writerow(info)

        quaternion = rot
        rpy=tf.transformations.euler_from_quaternion(quaternion)
       
        print 'translation vector: (',trans[0],',',trans[1],')'
       


        rate.sleep()