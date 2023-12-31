import rclpy                     #ROS2のクライアントのためのライブラリ
from rclpy.node import Node
from std_msgs.msg import Int16 #使う型を変更

class Talker():
    def _init_(self):
        self.pub = node.create_publisher(Int16, "countup", 10)
        self.n = 0


rclpy.init()
node = Node("talker")
talker = Talker()

def cb():
     msg = Int16()         #受信するデータの型を変更
     msg.data = talker.n  #msgファイルに書いた「name」
     talker.pub.publish(msg)
     talker.n += 1

node.create_timer(0.5, cb)
rclpy.spin(node)
