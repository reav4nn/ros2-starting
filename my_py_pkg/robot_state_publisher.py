#!/usr/bin/env python3

from example_interfaces.msg import String
import rclpy
from rclpy.node import Node

class MyRobotStatePublisher(Node):
    def __init__(self):
        super().__init__('my_robot_state_publisher')

        self.publisher_ = self.create_publisher(String, 'robot_state', 10)
        self.timer = self.create_timer(1.0, self.publish_state)

        self.get_logger().info('MyRobotStatePublisher node has been started.')

    def publish_state(self):
        msg = String() # creating a new String message instance
        msg.data = 'Robot state at time {}'.format(self.get_clock().now().to_msg()) # setting the data field of the message to a string that includes the current time
        self.publisher_.publish(msg) # publishing the message to the 'robot_state' topic

def main(args=None):
    rclpy.init(args=args)

    node = MyRobotStatePublisher()
    rclpy.spin(node)

    rclpy.shutdown()

if __name__ == '__main__':
    main()