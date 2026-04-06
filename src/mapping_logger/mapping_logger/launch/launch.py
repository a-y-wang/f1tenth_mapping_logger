from launch import LaunchDescription
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
                'image_size': [1920, 1200], # Your 2MP Resolution
                'pixel_format': 'MJPG',     # Required for 90fps
            }]
        ),

        # 2. Start VSLAM (Using RTAB-Map for Monocular)
        Node(
            package='rtabmap_slam',
            executable='rtabmap',
            name='rtabmap',
            parameters=[{
                'subscribe_depth': False,
                'subscribe_rgb': True,
                'approx_sync': True,
                'RGBD/Enabled': 'false',
                'VisualCompute/KeepImages': 'false', # Save memory on Rubik Pi
            }],
            remappings=[
                ('rgb/image', '/image_raw'),
            ]
        ),

        # 3. Start YOUR Logger Node
        Node(
            package='mapping_logger',
            executable='logger_node', # The name defined in setup.py
            name='csv_logger'
        )
    ])