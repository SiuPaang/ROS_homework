#!/usr/bin/env python
# -*- coding: utf-8 -*-
import rospy
import cv2
import numpy as np
from sensor_msgs.msg import Image, RegionOfInterest
from cv_bridge import CvBridge, CvBridgeError
from sound_play.msg import SoundRequest
from sound_play.libsoundplay import SoundClient
from std_msgs.msg import String

# 利用soundplay_node将人数发送出去
soundhandle = SoundClient()
rospy.sleep(1)

class face_number_teller:
    def __init__(self):
        self.output_faces_number = "0"
        self.faces_number_queue = []
        self.faces_number_sub = rospy.Subscriber("faces_number", String, self.callback)
    
    def callback(self, data):
        self.faces_number_queue.append((data.data))
        if len(self.faces_number_queue) == 10:
            # 下面这个判断条件是连续的10幅图像中所看到的人数相等，
            # 并且与上一个判断不相同
            if self.is_tell() != None and self.output_faces_number != self.is_tell():
                self.output_faces_number = self.is_tell()
                if self.output_faces_number == "2":
                    rospy.loginfo("current_number:%s",self.output_faces_number)
                    soundhandle.say("I saw two people")
                    for i in range(10):
                        self.faces_number_queue.pop()
                if self.output_faces_number == "1":
                    rospy.loginfo("current_number:%s",self.output_faces_number)
                    soundhandle.say("I saw one person")
                    for i in range(10):
                        self.faces_number_queue.pop()
                if self.output_faces_number == "0":
                    rospy.loginfo("current_number:%s",self.output_faces_number)
                    soundhandle.say("I saw no person")
                    for i in range(10):
                        self.faces_number_queue.pop()
            
            else:
                for i in range(10):
                    self.faces_number_queue.pop()

    # 判断10张图像中检测到的人数是否相等，需要这10幅图像中检测到的人数相等，才能下结论
    def is_tell(self):
        for i in range(len(self.faces_number_queue) - 1):
            if self.faces_number_queue[i] == self.faces_number_queue[i+1]:
                if i == 8:
                    return self.faces_number_queue[0]
            else:
                return
	

if __name__ == '__main__':
    rospy.init_node('face_number_teller',anonymous=True)
    face_number_teller()
    rospy.spin()
