import sqlite3
conn=sqlite3.connect('MitMorn.db')
print("Open database Successfully")
conn.execute("INSERT INTO wanafunziiii(ID,NAME,AGE,SCHOOL,GENDER)VALUES (1,'ERICK',30,'EMOBILIS','MALE')")
conn.execute("INSERT INTO wanafunziiii(ID,NAME,AGE,SCHOOL,GENDER)VALUES (4,'FREDY',90,'EMOBILIS','MALE')")
conn.execute("INSERT INTO wanafunziiii(ID,NAME,AGE,SCHOOL,GENDER)VALUES (7,'MOUNT',87,'EMOBILIS','MALE')")
conn.execute("INSERT INTO wanafunziiii(ID,NAME,AGE,SCHOOL,GENDER)VALUES (8,'REBBECCA',56,'EMOBILIS','MALE')")
conn.execute("INSERT INTO wanafunziiii(ID,NAME,AGE,SCHOOL,GENDER)VALUES (6,'MOSES',40,'EMOBILIS','MALE')")
conn.execute("INSERT INTO wanafunziiii(ID,NAME,AGE,SCHOOL,GENDER)VALUES (9,'COLLINS',23,'EMOBILIS','MALE')")

conn.commit()
print("Records added successfully")
conn.close()