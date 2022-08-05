import sqlite3
db=sqlite3.connect("mydatabase3.db")
curs=db.cursor()
db.execute("PRAGMA foreign_keys = ON")
curs.execute("""CREATE TABLE jobs(
40Job_id VARCHAR(255) PRIMARY KEY
);""")
curs.execute("""INSERT INTO jobs VALUES ('j1');""")
curs.execute("""INSERT INTO jobs VALUES('j2');""")
curs.execute("""INSERT INTO jobs VALUES('j3');""")
curs.execute("""CREATE TABLE job_history(
employeeid INTEGER NOT NULL,
startdate DATE NOT NULL,
enddate DATE NOT NULL,
job_id VARCHAR(255) NOT NULL,
departmentid INTEGER NOT NULL,
FOREIGN KEY (job_id) REFERENCES jobs(Job_id)
);""")
curs.execute("""INSERT INTO job_history VALUES('1','2000-02-20','2010-02-20','j1','01');""")
curs.execute("""INSERT INTO job_history VALUES('2','2005-10-09','2016-05-10','j2','02');""")
curs.execute("""INSERT INTO job_history VALUES('5','1990-05-11','1995-06-19','j1','10');""")
curs.execute("""INSERT INTO job_history VALUES('23','1998-02-15','2011-10-12','j3','05');""")
curs.execute("SELECT * FROM job_history where job_id='j1'")
res=curs.fetchall()
for i in res:
    print(i)
db.commit()
db.close()