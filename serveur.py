# Server giving xyz
import socket
import rospy
from geometry_msgs.msg import Twist
import time



def sendXYZ(stringXYZ):
  
  
  global begin
  if time.time()-begin > 0.9 :
    global conn
    print "brut",stringXYZ.linear.x , "parse int", int(1000*stringXYZ.linear.x)
    msg = str(-int(1000*stringXYZ.linear.y)) +";"+str(-int(1000*stringXYZ.linear.z))+";"+str(int(1000*stringXYZ.linear.x))+";"+str(-int(1000*stringXYZ.angular.x)) +";"+str(-int(1000*stringXYZ.angular.y))+";"+str(int(1000*stringXYZ.angular.z))+"\n"
    conn.sendall(msg)
    begin = time.time()

  time.sleep(0.1)

def resetConnexion():
  global conn, addr, sub, is_connected
  conn.close()
  addr=''
  sub.unregister()
  is_connected=False
  
rospy.init_node('serverXYZ', anonymous=True)

HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 50018              # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
is_connected=False
r=rospy.Rate(1)
data=None
is_Sub = False
begin=time.time()
while not rospy.is_shutdown() :
    if not is_connected:
      s.listen(1)
      conn, addr = s.accept()
      print ('Connected by',addr)
      is_connected=True
      if not is_Sub :
        sub = rospy.Subscriber("position_inf", Twist, sendXYZ, queue_size = 1)
        is_Sub=True
    else:
      want_exit=False
      """while not data:
        data = conn.recv(1024)"""
    
    r.sleep()
exit()


