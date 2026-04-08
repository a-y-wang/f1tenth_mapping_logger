from launch import LaunchDescription
from launch.actions import ExecuteProcess
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        # 1. Start the AR0234 USB Camera
        Node(
            package='v4l2_camera',
            executable='v4l2_camera_node',
            name='camera_node',
            parameters=[{
                'video_device': '/dev/video0',
                'image_size': [640, 480], # Your 2MP Resolution
                'pixel_format': 'MJPG',     # Required for 90fps
            }]
        ),

        # 2. Start ORB-SLAM and PIPE it into Andy's Bridge
        # change momo_live to whatever VSLAM executable you are using
        ExecuteProcess(
            cmd=['./mono_live | ros2 run orbslam_bridge bridge_node'],
            shell=True
        ),


        # 3. Start YOUR Logger Node
        Node(
            package='mapping_logger',
            executable='logger_node', # The name defined in setup.py
            name='csv_logger'
        )
    ])