#!/usr/bin/python
import rospy
import aiml
import os
import sys
from std_msgs.msg import String

def callback(data):
    chat_input = data.data
    response = chat_aiml.respond(chat_input)
    rospy.loginfo("I heard: %s", data.data)
    rospy.loginfo("I spoke: %s", response)

    response_pub.publish(response)

def listener():
    rospy.loginfo("Starting ROS AIML voice Server")
    rospy.Subscriber("chat_data", String, callback)
    rospy.sleep(5.)
    rospy.spin()

if __name__ == '__main__':
    rospy.init_node('chat_match')
    chat_aiml = aiml.Kernel()
    chat_aiml.learn("/home/siupaang/rse_ws/src/robot_voice/aiml_data/chat_dialog.aiml")

    response_pub = rospy.Publisher('response', String, queue_size=10)
    listener()
    
