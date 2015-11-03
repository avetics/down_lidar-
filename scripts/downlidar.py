#!/usr/bin/env python
import rospy
from struct import *
from mavros_msgs.msg import Mavlink
import string
import threading
from std_msgs.msg import Float64


def downlidar():
   
    
    pub = rospy.Publisher('down_lidar', Float64, queue_size = 10)
    rospy.init_node('downlidar', anonymous=True)
    #rate = rospy.Rate(10) # 10hz
   
    def mavCallback(data):
         if int(data.msgid) == 173:
            p = pack("i", data.payload64[0])
            distance = unpack("f",p)
	   # while not rospy.is_shutdown():
		#rospy.loginfo(hello_str)
	    pub.publish(distance[0])
		#rate.sleep()
    def listener():
	rospy.Subscriber("/mavlink/from", Mavlink, mavCallback)
        rospy.spin()

    update = threading.Thread(target = listener) 
    update.start()
            
  

  

        

if __name__ == '__main__':
    try:
        downlidar()
      
    except rospy.ROSInterruptException:
        pass

   
