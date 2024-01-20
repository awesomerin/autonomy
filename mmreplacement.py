import rclpy
from rclpy.node import Node
from sensor_msgs.msg import PointCloud2
import sensor_msgs.point_cloud2 as pc2

class PointCloudSubscriber(Node):

    def __init__(self):
        super().__init__('point_cloud_subscriber')
        self.subscription = self.create_subscription(
            PointCloud2,
            'mos_point_cloud',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        #self.get_logger().info('Received a point cloud')
        for p in pc2.read_points(msg, field_names=("x", "y", "z"), skip_nans=True):
            print("x:", p[0], "y:", p[1], "z:", p[2])

def main(args=None):
    rclpy.init(args=args)

    print("create subscriber")
    subscriber = PointCloudSubscriber()
    print("subscriber created")
    rclpy.spin(subscriber)
    print("subscriber started")
    # Clean up and shut down gracefully
    subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
