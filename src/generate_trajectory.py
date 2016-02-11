#!/usr/bin/env python

from openravepy import *
from shared_global import *
import numpy as np
import rospy
import sys
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg

class GenerateTrajectory():
    def __init__(self):
        self.name = "hello"

if __name__=="__main__":
    moveit_commander.roscpp_initialize(sys.argv)
    rospy.init_node("generate_trajectory",anonymous = True)
    robot = moveit_commander.RobotCommander()
    scene = moveit_commander.PlanningSceneInterface()
    display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path',moveit_msgs.msg.DisplayTrajectory)
    rospy.sleep(10)
    trajectory =  GenerateTrajectory()
