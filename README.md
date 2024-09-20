# MathEGE

## Description
A university project in Django, aimed at studying the technology of this framework, as well as studying backend solutions, including registration and authorization, the process of testing backend code and also the frontend of frameworks (bootstrap). Work with databases for storing user data was implemented.

## Instalation
1. Clone repository <br>
  `git clone https://github.com/Str0ng1ch/MathEGE.git`
2. Install dependencies <br>
    1. Install using command `pip install -r requirements.txt`
    2. Navigate to the project directory `cd MathEGE`
    3. |   Libraries     |               Purpose                  |  Version  |        Installation             |
       |:---------------:|:--------------------------------------:|:---------:|:-------------------------------:|
       |      Django     |     framework for web development      |   4.2.6   | pip install Django==4.2.6       |
       |   mysqlclient   |       Python interface to MySQL        |   2.2.0   | pip install mysqlclient==2.2.0  |
    4. Run migrations `python manage.py migrate`

## Launch
  1. To start the development server, run: `python MathEGE/manage.py runserver`

## Usage
  1. Go to localhost (`http://localhost/` or `http://127.0.0.1/`) and enjoy website.

## Technologies Used
1. `Django` – Backend framework for building the application.
2. `Bootstrap` – Frontend framework for responsive design.
3. `MySQL` – Relational database management system.
4. `mysqlclient` – Interface for connecting Django to MySQL.
5. `HTML/CSS/JavaScript` – Frontend technologies.

## Contributing
Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new feature branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.
