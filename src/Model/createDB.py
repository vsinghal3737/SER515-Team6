import sqlite3

connection = sqlite3.connect('app.db')
cursor = connection.cursor()


create_table_UserAuth = "CREATE TABLE IF NOT EXISTS UserAuth (AuthID INTEGER PRIMARY KEY, username text not null UNIQUE, password text not null, UserAuth_UserID int not null)"
create_table_User = "CREATE TABLE IF NOT EXISTS User (UserID INTEGER PRIMARY KEY, FirstName text not null, LastN text, Email text UNIQUE not null, Phone INTEGER UNIQUE, Grade text, Role text)"
create_table_Question = "CREATE TABLE IF NOT EXISTS Question (QuestionID INTEGER PRIMARY KEY, Question text not null, Answer text not null, Grade text not null, ProfID int, SubmittedOn date)"
create_table_HistoryQues = "CREATE TABLE IF NOT EXISTS HistoryQues (HisID INTEGER PRIMARY KEY, StudentID INTEGER not null, HISID_QuestionID INTEGER not null, AttemptedAns text, Result text, SubmittedOn date)"


cursor.execute(create_table_UserAuth)
cursor.execute(create_table_User)
cursor.execute(create_table_Question)
cursor.execute(create_table_HistoryQues)


cursor.execute("INSERT INTO UserAuth VALUES (1, 'admin', 'password', 1)")
cursor.execute("INSERT INTO User VALUES (1, 'admin', null, 'SER515.TEAM6@gmail.com', null, null, null)")


connection.commit()
connection.close()


# .open src\Model\database.db
