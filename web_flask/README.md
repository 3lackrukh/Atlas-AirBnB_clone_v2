# Flask Web Application

This project is a web application built using the Flask framework in Python. It demonstrates the use of various Flask features, including routing, templates, and database integration with MySQL.

## Learning Objectives

By completing this project, you will gain an understanding of the following concepts:

- What is a Web Framework
- How to build a web framework with Flask
- How to define routes in Flask
- What is a route
- How to handle variables in a route
- What is a template
- How to create an HTML response in Flask by using a template
- How to create a dynamic template (loops, conditions, etc.)
- How to display data from a MySQL database in HTML

## Prerequisites

Before running this application, ensure that you have the following installed:

- Python 3.x
- Flask
- MySQL

## Installation

1. Clone the repository:

Copy

Insert at cursor
markdown
git clone https://github.com/your-username/flask-web-app.git


2. Navigate to the project directory:

Copy

Insert at cursor
text
cd flask-web-app


3. Install the required Python packages:

Copy

Insert at cursor
text
pip install -r requirements.txt


4. Set up the MySQL database by running the provided SQL script:

Copy

Insert at cursor
text
mysql -u root -p < database.sql


5. Configure the database connection settings in `app.py`.

## Usage

To run the Flask application, execute the following command:

Copy

Insert at cursor
text
flask run


The application will be accessible at `http://localhost:5000`.

## Project Structure

- `app.py`: The main Flask application file, containing routes and database integration.
- `templates/`: Directory for HTML templates.
- `static/`: Directory for static files (CSS, JavaScript, images).
- `database.sql`: SQL script for creating the MySQL database and tables.
