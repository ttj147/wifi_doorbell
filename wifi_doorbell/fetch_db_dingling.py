#!/depot/Python-2.5/bin/python
#coding = utf-8
import sqlite3
import SocketServer

def get_door_status(name):
	name = 'DingLing'
	conn = sqlite3.connect('dingling.db')
	c = conn.cursor() 
	rec = c.execute('''SELECT * FROM doorTable WHERE name=(?) AND tdatetime > datetime('now','localtime','-0.5 hours') ORDER BY tdatetime ASC;''',(name, ))
	out = c.fetchall()

	if out:
		print "hello"
#		print out
	else:		
		rec = c.execute('''SELECT * FROM doorTable WHERE name=(?) AND tdatetime > datetime('now','localtime','-8 hours') ORDER BY tdatetime ASC;''',(name, ))
		out = c.fetchall()
    
	conn.close()
	return out


class MyTCPHandler(SocketServer.BaseRequestHandler):
    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
#        print "{} wrote:".format(self.client_address[0])
#        print self.data
#        print 'send to client door status'
        status = get_door_status('DingLing')
        if status:
            for m in status:	
                a = ','.join(m)+';\n'
                self.request.sendall(a)
        else:
            a ='not changed'
            self.request.sendall(a)		
		
if __name__ == '__main__':
    HOST, PORT = "192.168.123.136", 9998

    # Create the server, binding to localhost on port 9999
    server = SocketServer.TCPServer((HOST, PORT), MyTCPHandler)

    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server.serve_forever()
