#!/usr/bin/env python  
# -*- coding: utf-8 -*-  
import time  
import sqlite3  
import SocketServer
  
def get_cpu_temp():  
    # 打开文件  
    file = open("/sys/class/thermal/thermal_zone0/temp")  
    # 读取结果，并转换为浮点数  
    temp = float(file.read()) / 1000  
    # 关闭文件  
    file.close()  
    return temp  
  
def insert_cpu_temp(temp):  
    # 连接数据库  
    conn=sqlite3.connect('dingling.db')  
    curs=conn.cursor()    
      
    # 插入数据库  
    #strtemp = "%.1f" %(temp);  
    curs.execute("INSERT INTO doorTable(door_status) VALUES((?))",(temp,))  
    conn.commit()  
      
    # 关闭数据库  
    conn.close()  

def main():  
    while True:  
        temp = get_cpu_temp()  
        #insert_cpu_temp(temp)  
        print "insert one"
        time.sleep(1*60)  

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
        print "{} wrote:".format(self.client_address[0])
        print self.data
        print "insert data to dadabase"
        insert_cpu_temp(self.data) 
        # just send back the same data, but upper-cased
        self.request.sendall(self.data.upper())
		#main() 
		
		
		
if __name__ == '__main__':
    HOST, PORT = "192.168.123.136", 9999

    # Create the server, binding to localhost on port 9999
    server = SocketServer.TCPServer((HOST, PORT), MyTCPHandler)

    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server.serve_forever()
		
