#!/usr/bin/env python3

from example_interfaces.msg import String
import rclpy
from rclpy.node import Node

class MyRobotStatePublisher(Node):
    def __init__(self):
        super().__init__('my_robot_state_publisher')

        self.publisher_ = self.create_publisher(String, 'robot_state', 10)

def main(args=None):
    rclpy.init(args=args)

    node = MyRobotStatePublisher()
    rclpy.spin(node)

    rclpy.shutdown()

if __name__ == '__main__':
    main()