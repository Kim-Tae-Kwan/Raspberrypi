# 라즈베리파이
# SQLite3 실습

from sys import argv
import csv
import sqlite3

conn=sqlite3.connect('sample.db')
c=conn.cursor()

if len(argv)<2: # 아규먼트 에러
    print("Please provide a name of a csv file")
    exit(1)
else:#정상적인 실행
    csvfile=argv[1]
    print(csvfile)

    #테이블
    c.execute("CREATE TABLE IF NOT EXISTS student ( id INTEGER PRIMARY KEY AUTOINCREMENT,\
                name TEXT, birth DATE,gender CHAR)") 

    list_a[3]
    for 
    a=input("입력하세요 > ")
    list_a[]=a

    

    #student=csv.reader(open(csvfile,'r'),delimiter=',',quotechar='"')
    #index=0
    
    # for row in student:
    #     #index+=1
    #     print("{}".format(row))
    #     c.execute("INSERT INTO student(name,birth,gender) VALUES(?,?,?)",(row[0],row[1],row[2]))


    conn.commit()
    conn.close()
    exit()
