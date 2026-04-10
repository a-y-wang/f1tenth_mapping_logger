import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PoseStamped
import csv
import os

class PoseToCSV(Node):
    def __init__(self):
        super().__init__('pose_to_csv')
        # VSLAM usually publishes to /rtabmap/localization_pose or similar
        self.sub = self.create_subscription(PoseStamped, '/odom', self.callback, 10)
        self.file_path = os.path.expanduser('~/track_data.csv')
        self.file = open(self.file_path, 'w')
        self.writer = csv.writer(self.file)
        self.writer.writerow(['timestamp', 'x', 'y', 'z'])

    def callback(self, msg):
        p = msg.pose.position  # Simplified path since there is no .pose.pose
        t = msg.header.stamp.sec + msg.header.stamp.nanosec * 1e-9
        self.writer.writerow([t, p.x, p.y, p.z])

def main():
    rclpy.init()
    node = PoseToCSV()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass

    node.file.close()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
