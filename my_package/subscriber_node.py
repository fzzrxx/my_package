#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int64

class NumberSubscriber(Node):
    def __init__(self):
        super().__init__('number_subscriber')
        self.subscription = self.create_subscription(
            Int64,
            'number',
            self.callback,
            10
        )

    def callback(self, msg):
        self.get_logger().info(f'Received: {msg.data}')

def main():
    rclpy.init()
    node = NumberSubscriber()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()