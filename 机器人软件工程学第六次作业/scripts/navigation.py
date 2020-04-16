#!/usr/bin/env python

import rospy

import actionlib
from actionlib_msgs.msg import *
from geometry_msgs.msg import Pose, PoseWithCovarianceStamped, Point, Quaternion, Twist
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from tf.transformations import quaternion_from_euler
from std_msgs.msg import String

class NavToPoint:
    def __init__(self):
        # rospy.on_shutdown(self.cleanup)
	self.start = 0
	self.original = 0
	
	rospy.Subscriber("chat_data", String, self.callback)
	self.A = 'none'
        
	# Subscribe to the move_base action server
        self.move_base = actionlib.SimpleActionClient("move_base", MoveBaseAction)
        rospy.loginfo("Waiting for move_base action server...")

        # Wait for the action server to become available
        self.move_base.wait_for_server(rospy.Duration(120))
        rospy.loginfo("Connected to move base server")

        # A variable to hold the initial pose of the robot to be set by the user in RViz
        initial_pose = PoseWithCovarianceStamped()
        rospy.Subscriber('initialpose', PoseWithCovarianceStamped, self.update_initial_pose)

	# Get the initial pose from the user
        rospy.loginfo("*** Click the 2D Pose Estimate button in RViz to set the robot's initial pose...")
        rospy.wait_for_message('initialpose', PoseWithCovarianceStamped)
        
        # Make sure we have the initial pose
        while initial_pose.header.stamp == "":
        	rospy.sleep(1)
            
        rospy.loginfo("Ready to go")
	rospy.sleep(1)

	# 3 Locations, bookshelf,barrier,cube
	locations = dict()
	bookshelf_x = -0.144
	bookshelf_y = 0.617
	bookshelf_theta = 1.5708
	quaternion1 = quaternion_from_euler(0.0, 0.0, bookshelf_theta)
	locations['bookshelf'] = Pose(Point(bookshelf_x, bookshelf_y, 0.000), Quaternion(quaternion1[0], quaternion1[1], quaternion1[2], quaternion1[3]))

	cube_x = 0.412
	cube_y = -0.393
	cube_theta = 1.5708
	quaternion2 = quaternion_from_euler(0.0, 0.0, cube_theta)
	locations['cube'] = Pose(Point(cube_x, cube_y, 0.000), Quaternion(quaternion2[0], quaternion2[1], quaternion2[2], quaternion2[3]))

	barrier_x = -2.82
	barrier_y = -0.63
	barrier_theta = 1.5708
	quaternion3 = quaternion_from_euler(0.0, 0.0, barrier_theta)
	locations['barrier'] = Pose(Point(barrier_x, barrier_y, 0.000), Quaternion(quaternion3[0], quaternion3[1], quaternion3[2], quaternion3[3]))

	self.goal = MoveBaseGoal()
        rospy.loginfo("Starting navigation test")

	while not rospy.is_shutdown():
	  self.goal.target_pose.header.frame_id = 'map'
	  self.goal.target_pose.header.stamp = rospy.Time.now()
	 
	  # Robot will go to point A
	  if self.start == 1:
		rospy.loginfo("Going to " + self.A)
		rospy.sleep(2)
		
		self.goal.target_pose.pose = locations[self.A]
	  	self.move_base.send_goal(self.goal)
		waiting = self.move_base.wait_for_result(rospy.Duration(300))
		if waiting == 1:
		    rospy.loginfo("Reached")
		    rospy.sleep(2)
		    self.start = 0

	  rospy.Rate(5).sleep()


    def callback(self, data):
	if data.data == 'GO TO THE BARRIER':
		self.A = 'barrier'
		self.start = 1
	elif data.data == 'GO TO THE CUBE':
		self.A = 'cube'
		self.start = 1
	elif data.data == 'GO TO THE BOOKSHELF':
		self.A = 'bookshelf'
		self.start = 1

    def update_initial_pose(self, initial_pose):
        self.initial_pose = initial_pose
	if self.original == 0:
		self.origin = self.initial_pose.pose.pose
		self.original = 1

    def cleanup(self):
        rospy.loginfo("Shutting down navigation	....")
	self.move_base.cancel_goal()

if __name__=="__main__":
    rospy.init_node('navi_point')
    NavToPoint()
    rospy.spin()


