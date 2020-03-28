#!/usr/bin/env python
'''
This node subscribe topic "chat_data" from picture_voice_recognize.py and 
"/usb_cam/image_raw".When this node receive the string information "cheese",
this node then picture according the data of "/usb_cam/image_raw" and save in 
the given path.
'''

from __future__ import print_function
import sys
import rospy
import cv2
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import time

class TakePhoto:
    def __init__(self):
        self.bridge = CvBridge()
        self.is_picture = False
        image_topic = "/usb_cam/image_raw"

        self.image_sub = rospy.Subscriber(image_topic, Image, self.imageCallback)
        self.action_signal_sub = rospy.Subscriber("action_signal", String, self.chatdataCallback)
        self.success_pub = rospy.Publisher('success_signal', String, queue_size = 5)

        self.success_signal = "I have taken one photo for you"
        rospy.sleep(1)
    
    def chatdataCallback(self,data):
        if data.data == 'CHEESE':
            ###############choose your picture save path%%%%%%%%%%%%%%
            path = "/home/siupaang/rse_ws/src/robot_vision/photos/"
            timestr = time.strftime("%Y%m%d-%H%M%S-")
            img_title = path + timestr + "photo.jpg"
            self.take_picture(img_title)


    def imageCallback(self,data):
        # Convert image to OpenCV format
        try:
            cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
        except CvBridgeError as e:
            print(e)

        self.image_received = True
        self.image = cv_image

    def take_picture(self, img_title):
        if self.image_received:
            # Save an image
            cv2.imwrite(img_title, self.image)
            self.success_pub.publish(self.success_signal)
            return True
        else:
            return False

if __name__ == '__main__':
    rospy.init_node('photo_taker', anonymous=False)
    takephoto = TakePhoto()

    rospy.spin()