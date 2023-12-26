import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16

class Talker():
    def _init_(self):
        self.pub = node.create_publisher(Int16, "countup" , 10)
        self.n = 0

rclpy.init()
node = Node("listener")
pub = node.create_subscription(Int16, "countup", cb, 10)
rclpy.spin(node)
