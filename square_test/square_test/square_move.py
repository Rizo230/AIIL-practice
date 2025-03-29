import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import time
import math
class MoveRoverSquare(Node):
    def __init__(self):
        super().__init__('move_rover_square')
        self.publisher = self.create_publisher(Twist, '/cmd_vel', 10)
        self.move_square()
    
    # move straight ahead
    def move_straight(self, distance=3, speed=0.5):
        print("Moving forward")
        action = Twist()
        pause_time = distance/speed
        action.linear.x = speed
        self.publisher.publish(action) #move ahead
        time.sleep(pause_time)
        action.linear.x = 0.0
        self.publisher.publish(action) #stop moving
    
    #turn 90 degrees
    def turn_corner(self, angle=90, speed=0.5):
        print("Turning")
        radians = math.radians(angle)
        pause_time = 9
        action = Twist()
        action.linear.x = 0.0
        action.angular.z = speed
        self.publisher.publish(action) 
        time.sleep(pause_time)
        action.angular.z = 0.0
        self.publisher.publish(action) #stop moving
    
    #move in a square shape
    def move_square(self):
        for i in range(0,4):
            self.move_straight()
            self.turn_corner()
  
def main(args=None):
    print("Starting Node")
    rclpy.init(args=args)
    move_rover = MoveRoverSquare()
    rclpy.spin(move_rover)
    

if __name__ == '__main__':
    main()