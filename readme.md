# SER 515 F19 - Project

Team 6
## Team Members:
- Ankit Vutukuri
- Mayank Batra
- Suraj Atmakuri
- Sneha Lakshminarasimhan
- Vaibhav Singhal


## How to run the Project

If python, pip is installed in your system skip first 2 steps

1.	To download Python: [click here](https://www.python.org/downloads/)
	install the software as mentioned in it, and add its path to the system environment variable

2. 	To download Pip: [click here](bootstrap.pypa.io/get-pip.py)
	save the file `ctrl+s` (file should save in .py format)
	open command prompt in the download location: `python get-pip.py`

3.	To download Libraries in your system
	Type in the command prompt: `pip install Flask Flask-JWT Flask-JWT-Extended Flask-RESTful Flask-SQLAlchemy`

3.1	To check if everything installed properly
	In command prompt: `python`
	In Python console: `import flask, flask_jwt, flask_jwt_extended, flask_restful, flask_sqlalchemy`

	If there is no error, Project Setup is Done.

4. To run the project:
	Open Command Prompt and navigate to project DIR where app.py file is located and type:
	`python app.py`

	In the web browser type `localhost:5000/` to start using the web interface of the project
