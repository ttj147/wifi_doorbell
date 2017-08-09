#!/usr/bin/env python  
# -*- coding: utf-8 -*-  
import time  
import sqlite3  
  
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
    strtemp = "%.1f" %(temp);  
    curs.execute("INSERT INTO doorTable(door_status) VALUES((?))",(strtemp,))  
    conn.commit()  
      
    # 关闭数据库  
    conn.close()  

def main():  
    while True:  
        temp = get_cpu_temp()  
        insert_cpu_temp(temp)  
        print "insert one"
        time.sleep(5*60)  
  
if __name__ == '__main__':  
	
    print "insert task..."  
    main()  
