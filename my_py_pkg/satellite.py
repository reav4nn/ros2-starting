#!/usr/bin/env python3

from my_py_pkg.my_first_node import MyFirstNode
from example_interfaces.msg import String
import rclpy
from rclpy.node import Node

class Satellite(Node):
    def __init__(self):
        super().__init__('satellite')

        self.subscriber_ = self.create_subscription(String, 'robot_state', self.callback_satellite, 10)        
        self.get_logger().info('Satellite has been started.')

    def callback_satellite(self, msg):
        self.get_logger().info(f'Satellite received: {msg.data}')

def main(args=None):
    rclpy.init(args=args)

    node = Satellite()
    rclpy.spin(node)

    rclpy.shutdown()

if __name__ == '__main__':
    main()