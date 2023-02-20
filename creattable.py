import sqlite3
conn=sqlite3.connect('MitMorn.db')
print("Open database Successfully")
conn.execute("CREATE TABLE wanafunziiii"
             " (ID INT PRIMARY KEY NOT NULL,"
             "NAME TEXT NOT NULL,"
             "AGE INT NOT NULL ,"
             "SCHOOL TEXT NOT NULL, "
             "GENDER TEXT NOT NULL)")
print("Tables created successfully")
conn.close()