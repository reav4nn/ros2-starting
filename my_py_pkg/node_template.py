#!/usr/bin/env python3

from my_py_pkg.my_first_node import MyFirstNode
from example_interfaces.msg import String
import rclpy
from rclpy.node import Node

class TemplateNode(Node): # TO DO: Change the class name
    def __init__(self):
        super().__init__('template_node') # TO DO: Change the node name

def main(args=None):
    rclpy.init(args=args)

    node = TemplateNode() # TO DO: Change the node name
    rclpy.spin(node)

    rclpy.shutdown()

if __name__ == '__main__':
    main()