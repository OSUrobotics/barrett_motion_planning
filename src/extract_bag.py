#!/usr/bin/env python

import rosbag
import rospkg
import getpass
from geometry_msgs.msg import PoseStamped
import numpy as np
import csv

if __name__ == "__main__":
    bag = rosbag.Bag('/home/saurabh/barrett_motion_capture/barrett_motion_capture.bag')
    messages = bag.read_messages(topics = "/wam/pose")
    output_file = open("barrett_robot_data.csv",'a')
    csv_writer = csv.writer(output_file)
    messages = bag.read_messages()
    for i in range(bag.get_message_count()):
        msg = messages.next()[1]
        time_stamp = msg.header.stamp
        x = msg.pose.position.x
        y = msg.pose.position.y
        z = msg.pose.position.z
        csv_writer.writerow([time_stamp,x,y,z])

    bag.close()
    output_file.close()
