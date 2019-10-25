'''

DO NOT RUN THIS FILE

'''

import sqlite3

connection = sqlite3.connect('app.db')
cursor = connection.cursor()

createTable = [

    "CREATE TABLE IF NOT EXISTS UserAuth (AuthID INTEGER PRIMARY KEY, username text not null UNIQUE, password text not null, UserAuth_UserID int not null)",
    "CREATE TABLE IF NOT EXISTS User (UserID INTEGER PRIMARY KEY, FName text not null, LName text, Email text UNIQUE not null, Phone INTEGER UNIQUE, Grade text, Role text)",
    "CREATE TABLE IF NOT EXISTS Question (QuestionID INTEGER PRIMARY KEY, Question text not null, Answer text not null, Grade text not null, ProfID int, SubmittedOn date)",
    "CREATE TABLE IF NOT EXISTS HistoryQues (HisID INTEGER PRIMARY KEY, StudentID INTEGER not null, HISID_QuestionID INTEGER not null, AttemptedAns text, Result text, SubmittedOn date)"
]

for query in createTable:
    cursor.execute(query)


# For Testing
# dropTable = [
#     "DROP TABLE UserAuth",
#     "DROP TABLE User",
#     "DROP TABLE Question",
#     "DROP TABLE HistoryQues"
# ]

# for query in dropTable:
#     cursor.execute(query)

cursor.execute("INSERT INTO User (FName, Email) VALUES ('admin', 'SER515.TEAM6@gmail.com')")
cursor.execute("INSERT INTO UserAuth (username, password, UserAuth_UserID) VALUES ('admin', 'password', 1)")


connection.commit()
connection.close()


# .open src\Model\database.db
