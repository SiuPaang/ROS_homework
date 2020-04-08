# 语音加图像的相关工作
------------------------------
## voice_control_picture.mp4 展示的是第一个工作
运行usb_cam-test.launch以及该功能包中的voice_control_picture.launch

usb_cam-test.launch打开电脑摄像头，voice_control_picture.launch先后打开下列一些节点

- picture_action_recognizer.py，基于pocketsphinx识别拍照信号"cheese"，发布/action_signal (String类型) 话题
- picture_taker.py，订阅"/usb_cam/image_raw" (Image类型) 以及"/action_signal“ (String类型) 两个话题，该节点接收到“/action_signal”话题消息为cheese时，拍下当时"/usb_cam/image_raw" 接收到的图像信息，并保存在该功能包的photos文件夹中，该节点在成功拍下照时，在“/success_signal”话题发布String类型的消息“I have taken one picture for you”
- picture_talkbacker.py，订阅“/success_signal”，然后将其消息发送给soundplay_node转换为语音
- soundplay_node.py
#### voice_control_picture_rqt_graph.png 是该工作运行时全部节点与话题的相互关系

## face_detect.mp4 展示的是第二个工作
运行usb_cam-test.launch以及该功能包中的face_detector.launch两个文件

face_detector.launch先后打开下面一些节点

- face_detector.py，此文件在胡春旭书的源码中，这个节点原来功能是订阅摄像头送出消息，进行人脸的检测，我在此基础上添加发送检测到的人脸数量话题“faces_number”
- face_number_teller.py，订阅"faces_number"话题，检测连续十张图像检测到的人脸数是否相同，再由soundplay节点语音输出
- soundplay_node.py
#### face_detector.png 是该工作运行时全部节点与话题的相互关系

# English Version
# some works relevant to ros speech and vision
------------------------------
## voice_control_picture.mp4 shows the first work
launch usb_cam-test.launch and voice_control_picture.launch in this package

usb_cam-test.launch open the PC camera while voice_control_picture.launch runs these nodes as follow:

- picture_action_recognizer.py，base on pocketsphinx, recognize the signal "cheese"，publish the topic /action_signal
- picture_taker.py，subscribe the topics "/usb_cam/image_raw" and "/action_signal“ ，when this node receive cheese from “/action_signal”，record one image from the topic "/usb_cam/image_raw"，and save it in photos.After that，publish “I have taken one picture for you” to the topic “/success_signal”
- picture_talkbacker.py，subscribe “/success_signal”，then publish the received messages to soundplay_node
- soundplay_node.py
#### voice_control_picture_rqt_graph.png is the rqt_graph

## face_detect.mp4 shows the second work
launch usb_cam-test.launch and face_detector.launch

face_detector.launch runs these nodes as follow:

- face_detector.py，subscribe "/usb_cam/image_raw" and detect face, then publish faces number to topic "face_number"
- face_number_teller.py，subscribe topic "faces_number"，Once 10 consecutive faces number are the same and it's different to the previous value, it would publish the value to soundplay
- soundplay_node.py
#### face_detector.png is the rqt_graph

