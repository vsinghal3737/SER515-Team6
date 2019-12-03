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
	Install the software as mentioned in it, and add its path to the system environment variable

2. 	To download Pip: [click here](https://bootstrap.pypa.io/get-pip.py)  
	Save the file `ctrl+s` (file should save in .py format)  
	Open command prompt in the download location: `python get-pip.py`

3.	To install Libraries that used in the project  
	Type in the command prompt: `pip install Flask Flask-SQLAlchemy Flask-Login Flask-RESTful Flask-MongoAlchemy`

4.	To check if everything installed properly  
	In command prompt: `python`  
	In Python console: `import flask, flask_sqlalchemy, flask_login, flask_restful, flask_mongoalchemy`  
	**If you get no error, Project Setup is Done**

5. To run the project:  
	Open Command Prompt and navigate to project DIR where app.py file is located  
	Type: `python app.py`  
	In the web browser type `localhost:5000/` to start using the web interface of the project  

6. To check the DB (*Optional*):  
	Download sqlite3 (Precompiled Binaries for Windows 1.7MB): [click here](https://www.sqlite.org/download.html)  
	Unzip the files and Add the path of the folder to [System Environment Variable](https://docs.alfresco.com/4.2/tasks/fot-addpath.html)
