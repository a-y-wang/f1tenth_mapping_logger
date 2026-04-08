cmake_minimum_required(VERSION 3.8)
project(orbslam_bridge)

if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 17)
endif()

find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(geometry_msgs REQUIRED)

add_executable(bridge_node src/bridge_node.cpp)
target_link_libraries(bridge_node rclcpp::rclcpp geometry_msgs::geometry_msgs)

ament_package()