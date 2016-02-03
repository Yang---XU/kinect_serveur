import socket
import sys
import time

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 50013)
print >>sys.stderr, 'connecting to %s port %s' % server_address
sock.connect(server_address)

while(True):
	try:
	    time.sleep(1)
	    """
	    # Send data
	    message = 'This is the message.  It will be repeated.'
	    print >>sys.stderr, 'sending "%s"' % message
	    sock.sendall(message)"""

	    # Look for the response

	    #amount_expected = len(message)
	    
	    while True:
		data = sock.recv(1024)
		
		print >>sys.stderr, 'received "%s"' % data

	finally:
	    print >>sys.stderr, 'closing socket'
	    sock.close()
