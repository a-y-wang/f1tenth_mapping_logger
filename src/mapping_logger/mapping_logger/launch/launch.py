from launch import LaunchDescription
from launch.actions import ExecuteProcess
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([

        # Camera
        Node(
            package='v4l2_camera',
            executable='v4l2_camera_node',
            name='camera_node',
            parameters=[{
                'video_device': '/dev/video0',
                'image_size': [640, 480],
            }]
        ),

        # ORB-SLAM + bridge
        ExecuteProcess(
            cmd=[
                'bash', '-c',
                '/home/ubuntu/ros2_ws/src/ORB_SLAM3/Examples/Monocular/mono_live '
                '/home/ubuntu/ros2_ws/src/ORB_SLAM3/Vocabulary/ORBvoc.txt '
                '/home/ubuntu/ros2_ws/src/ORB_SLAM3/Examples/Monocular/camera_fast.yaml '
                '| ros2 run orbslam_bridge bridge_node '
                '--ros-args -r /orbslam/pose:=/odom'
            ],
            shell=True
        ),

        # Logger
        ExecuteProcess(
            cmd=[
                'python3',
                '/home/ubuntu/ros2_ws/src/orbslam_bridge/scripts/pose_to_csv.py'
            ]
        )
    ])
