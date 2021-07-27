#!/usr/bin/env python
import rospy
from nav_msgs.msg import Odometry
import csv
import time

c = 0

def poseCallback(odom_data):
    global c

    fieldnames = ["x_value", "y_value"]

    pose_message = odom_data.pose.pose
    x= pose_message.position.x
    y= pose_message.position.y

    c+=1
    
    if (c/2000 == 1):
        c=0
        with open('odom_data3.csv','a') as csv_file:
            csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            info = {
                "x_value": x,
                "y_value": y,
            }
            csv_writer.writerow(info)
            print(x,y)
      
if __name__ == '__main__':
    try:
        fieldnames = ["x_value", "y_value"]
        with open('odom_data2.csv','w') as csv_file:
            csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            csv_writer.writeheader()
        rospy.init_node('gen_csv', anonymous=True)
        position_topic = "p3dx/odom"
        while(1):
            pose_subscriber = rospy.Subscriber(position_topic, Odometry, poseCallback) 
            time.sleep(2)

    except rospy.ROSInterruptException:
        rospy.loginfo("node terminated.")