#include<sstream>
#include "ros/ros.h"
#include "std_msgs/String.h"

int main(int argc, char** argv)
{	
	// 初始化ROS节点
	ros::init(argc,argv,"talker");
	ros::NodeHandle nh;
	
	ros::Publisher chatter_pub = nh.advertise<std_msgs::String>("chatter", 1000);
	ros::Rate loop_rate(1);
	// 设置循环频率为1，

	while (ros::ok())
	{
		std_msgs::String msg;
		std::stringstream ss;
		ss << "1711510";
		msg.data = ss.str();
		
		// 在终端上显示msg信息
		ROS_INFO("%s", msg.data.c_str());
		chatter_pub.publish(msg);
		
		ros::spinOnce();
		loop_rate.sleep();
	}
	return 0;
}
