#!/usr/bin/env python

from openravepy import *
from shared_global import *
import numpy as np
import rospy

class GenerateTrajectory():
    def __init__(self):
        self.env= Environment()
        self.env.SetViewer('qtcoin')
        self.path = barrett_motion_planning_dir
        self.env.Load(self.path+"/robots/wam7.xml")
        self.robot = self.env.GetRobots()[0]
        RaveSetDebugLevel(DebugLevel.Debug)
        self.planner = RaveCreatePlanner(self.env, 'OMPL_RRTConnect')
        self.simplifier = RaveCreatePlanner(self.env, 'OMPL_Simplifier')
        self.params = Planner.PlannerParameters()
        self.params.SetRobotActiveJoints(self.robot)
        self.params.SetGoalConfig([-0.75,1.24,-0.064,2.33,-1.16,-1.548,1.19])
        self.params.SetExtraParameters('<range>0.02</range>')
        self.planner.InitPlan(self.robot,self.params)

        self.traj = RaveCreateTrajectory(self.env,'')
        self.result = self.planner.PlanPath(self.traj)
        assert self.result == PlannerStatus.HasSolution

        self.simplifier.InitPlan(self.robot, Planner.PlannerParameters())
        self.result = self.simplifier.PlanPath(self.traj)
        assert self.result == PlannerStatus.HasSolution

        self.result = planningutils.RetimeTrajectory(self.traj)
        assert self.result == PlannerStatus.HasSolution

        self.robot.GetController().SetPath(self.traj)
        while not rospy.is_shutdown():
            n=1

if __name__=="__main__":
    trajectory =  GenerateTrajectory()
