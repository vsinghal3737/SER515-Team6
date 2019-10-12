from flask import jsonify
import sqlite3


def addQuestion(questionDict):
    connection = sqlite3.connect('app.db')
    cursor = connection.cursor()

    for key in sorted(questionDict.keys()):
        cursor.execute(
            "INSERT INTO Question (Question, Answer, Grade, ProfID, SubmittedOn) VALUES (?,?,?,?,?)",
            [
                questionDict[key]['Question'],
                questionDict[key]['Answer'],
                questionDict[key]['Grade'],
                questionDict[key]['ProfID'],
                questionDict[key]['SubmittedOn'],
            ]
        )
    connection.commit()
    connection.close()


def getQuestion(grade):
    connection = sqlite3.connect('app.db')
    cursor = connection.cursor()
    questions = cursor.execute("SELECT * FROM Question where Grade=?", grade if type(grade) == str else int(grade)).fetchall()
    connection.commit()
    connection.close()
    return jsonify({'questions': {k: questions[k - 1] for k in range(1, len(questions) + 1)}})


DummyQuestions = {
    1: {
        'Question': '5 + 4 = _',
        'Answer': '9',
        'Grade': 1,
        'ProfID': '2',
        'SubmittedOn': '2019-10-12 21:33:48'
    },
    2: {
        'Question': '9 - 7 = _',
        'Answer': '2',
        'Grade': 1,
        'ProfID': '2',
        'SubmittedOn': '2019-10-12 21:34:48'
    },
    3: {
        'Question': '_ + _ = 6',
        'Answer': 'na',
        'Grade': 1,
        'ProfID': '2',
        'SubmittedOn': '2019-10-12 21:35:48'
    },
    4: {
        'Question': '3 + 4 = _',
        'Answer': '7',
        'Grade': 1,
        'ProfID': '2',
        'SubmittedOn': '2019-10-12 21:36:48'
    },
    5: {
        'Question': '_ - _ = 2',
        'Answer': 'na',
        'Grade': 1,
        'ProfID': '2',
        'SubmittedOn': '2019-10-12 21:37:48'
    }
}
# addQuestion(DummyQuestions)
