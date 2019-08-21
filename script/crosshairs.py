#!/usr/bin/env python
import cv2
import rospy
import cv_bridge

from sensor_msgs.msg import Image, CameraInfo
import math
import numpy as np

rospy.init_node("crosshairs")
pub = rospy.Publisher("/image_crosshairs", Image, queue_size = 1)

def callback(msg_image):
    bridge = cv_bridge.CvBridge()
    img = bridge.imgmsg_to_cv2(msg_image, desired_encoding='bgr8')
    #img = cv2.imread('./test.png')
    Nx = img.shape[0]
    Ny = img.shape[1]
    color = (0, 255, 0)
    img = cv2.line(img, (0, Nx/2), (Ny-1, Nx/2), color, 1)
    img = cv2.line(img, (Ny/2, 0), (Ny/2, Nx-1), color, 1)
    msg_image_processed = bridge.cv2_to_imgmsg(img, encoding='bgr8')
    pub.publish(msg_image_processed)

rospy.Subscriber("/kinect_head/rgb/image_color", Image, callback)
rospy.spin()
