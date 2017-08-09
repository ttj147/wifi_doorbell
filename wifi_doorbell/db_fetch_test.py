#!/depot/Python-2.5/bin/python
#coding = utf-8
import sqlite3
 
conn = sqlite3.connect('dingling.db')
 
c = conn.cursor()
 
rec = c.execute('''select * from doorTable''')
print c.fetchall()
