import rospy
import rospkg
import os
import getpass

barrett_motion_planning_dir = rospkg.RosPack().get_path('barrett_motion_planning')
catkin_ws_location = barrett_motion_planning_dir[:-28] 
