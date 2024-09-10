import sqlite3
import hashlib

def addUser(user, pwd, type):
    conn = sqlite3.connect('quiz.db')
    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS USER;")
    cursor.execute("""
        CREATE TABLE USER(
        user TEXT NOT NULL PRIMARY KEY,
        pass TEXT NOT NULL,
        type TEXT NOT NULL);""")
    cursor.execute('Insert into USER(user,pass,type) values("{0}","{1}","{2}");'.format(user, pwd, type))
    conn.commit()
    conn.close()

def addQuiz(id, release, expire, problem, tests, results, diagnosis, numb):
    conn = sqlite3.connect('quiz.db')
    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS QUIZ;")
    cursor.execute("""
        CREATE TABLE QUIZ(
        id INTEGER NOT NULL PRIMARY KEY,
        release TEXT NOT NULL,
        expire TEXT NOT NULL,
        problem TEXT NOT NULL,
        tests TEXT NOT NULL,
        results TEXT NOT NULL,
        diagnosis TEXT NOT NULL,
        numb INTEGER NOT NULL);""")
    cursor.execute('Insert into QUIZ(id,release,expire,problem,tests,results,diagnosis,numb) values({0},"{1}","{2}","{3}","{4}","{5}","{6}",{7});'.format(id, release, expire, problem, tests, results, diagnosis, numb))
    
    cursor.execute("DROP TABLE IF EXISTS USERQUIZ;")
    cursor.execute("""
        CREATE TABLE USERQUIZ(
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        userid TEXT NOT NULL,
        quizid INTEGER NOT NULL,
        sent TEXT NOT NULL,
        answer TEXT NOT NULL,
        result TEXT NOT NULL);""")
    conn.commit()
    conn.close()
    
with open('users.csv','r') as file:
  lines = file.read().splitlines()

for users in lines:
  (user, type) = users.split(',')
  print(user)
  print(type)
  addUser(user, hashlib.md5(user.encode()).hexdigest(), type)
  addQuiz(1, '2018-01-01 00:00:00', '2018-01-01 00:00:00', 'problem', 'tests', 'results', 'diagnosis', 1)
