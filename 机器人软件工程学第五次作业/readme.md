# 语音加图像的相关工作
------------------------------
## voice_control_picture.mp4 展示的是第一个工作
运行usb_cam-test.launch以及该功能包中的voice_control_picture.launch

usb_cam-test.launch打开电脑摄像头，voice_control_picture.launch先后打开下列一些节点

- picture_action_recognizer.py，基于pocketsphinx识别拍照信号"cheese"，发布/action_signal (String类型) 话题
- picture_taker.py，订阅"/usb_cam/image_raw" (Image类型) 以及"/action_signal“ (String类型) 两个话题，该节点接收到“/action_signal”话题消息为cheese时，拍下当时"/usb_cam/image_raw" 接收到的图像信息，并保存在该功能包的photos文件夹中，该节点在成功拍下照时，在“/success_signal”话题发布String类型的消息“I have taken one picture for you”
- picture_talkbacker.py，订阅“/success_signal”，然后将其消息发送给soundplay_node转换为语音
