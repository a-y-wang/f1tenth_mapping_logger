#include <rclcpp/rclcpp.hpp>
#include <geometry_msgs/msg/pose_stamped.hpp>

#include <iostream>
#include <sstream>

class BridgeNode : public rclcpp::Node
{
public:
    BridgeNode() : Node("orbslam_bridge")
    {
        pub_ = create_publisher<geometry_msgs::msg::PoseStamped>(
            "/orbslam/pose", 10);

        timer_ = create_wall_timer(
            std::chrono::milliseconds(50),
            std::bind(&BridgeNode::read_pose, this));
    }

private:
    void read_pose()
    {
        static std::string line;

        if(!std::getline(std::cin, line))
            return;

        std::stringstream ss(line);

        float x, y, yaw;

        if(!(ss >> x >> y >> yaw))
            return;

        auto msg = geometry_msgs::msg::PoseStamped();

        msg.header.frame_id = "map";
        msg.header.stamp = now();

        msg.pose.position.x = x;
        msg.pose.position.y = y;
        msg.pose.position.z = 0.0;

        msg.pose.orientation.x = 0.0;
        msg.pose.orientation.y = 0.0;
        msg.pose.orientation.z = sin(yaw/2.0);
        msg.pose.orientation.w = cos(yaw/2.0);

        pub_->publish(msg);

        RCLCPP_INFO(
            this->get_logger(),
            "Pose: %.2f %.2f %.2f",
            x, y, yaw
        );
    }

    rclcpp::Publisher<geometry_msgs::msg::PoseStamped>::SharedPtr pub_;
    rclcpp::TimerBase::SharedPtr timer_;
};

int main(int argc, char **argv)
{
    rclcpp::init(argc, argv);

    auto node = std::make_shared<BridgeNode>();

    rclcpp::spin(node);

    rclcpp::shutdown();
    return 0;
}