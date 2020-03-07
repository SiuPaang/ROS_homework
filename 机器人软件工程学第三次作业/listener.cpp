#include "ros/ros.h"
#include "std_msgs/String.h"


void chatterCallback(const std_msgs::String::ConstPtr& msg)
{
    	ROS_INFO("I heard: [%s]", msg->data.c_str());
}


int main(int argc, char **argv)
{
    	// 初始化ROS节点
    	ros::init(argc, argv, "listener");
    	ros::NodeHandle n;

    	//订阅chatter话题
    	ros::Subscriber sub = n.subscribe("chatter", 1000, chatterCallback);
    	ros::spin();

    	return 0;
}
