# AE_WebScrapper_Database_Flaskwebserver
(posted 09/10/23):

This web flask application was made to automate specific sales and data points from scraped data from an e-commerce website. 


## Table of Contents
1. Project Overview
2. Package Dependencies
3. Frameworks and Extensions
4. Files
5. Demo
6. Acknowledgment
7. Roadmap

## Project Overview

## Package Dependencies

#### Flask: 
A lightweight Python web framework used for building web applications.
#### pip install Flask


#### SQLAlchemy:
A SQL toolkit and Object-Relational Mapping (ORM) library for Python, used for database interaction.
#### pip install SQLAlchemy


#### Selenium: 
A browser automation tool used for web scraping and automating web interactions.
#### pip install selenium

## Frameworks and Extensions

#### Flask
Flask is a micro web framework for Python that is widely used for building web applications. It provides a simple and flexible way to create web apps and APIs. You can learn more about Flask by visiting the official documentation: Flask Documentation

#### SQLAlchemy
SQLAlchemy is an Object-Relational Mapping (ORM) library for Python that simplifies database interactions. It allows you to work with databases using Python classes and objects instead of writing raw SQL queries. You can find more information about SQLAlchemy here: SQLAlchemy Documentation

### Selenium
Selenium is a powerful browser automation tool that allows you to control web browsers programmatically. It's commonly used for tasks such as web scraping, automating repetitive tasks, and testing web applications. In this project, Selenium is used for web scraping American Eagle product data from a specified URL.

#### Flask-WTF
Flask-WTF is a Flask extension that integrates the popular WTForms library for handling web forms in your application. It provides tools for form validation, rendering, and CSRF protection. Explore Flask-WTF: Flask-WTF Documentation

#### Flask-SQLAlchemy
Flask-SQLAlchemy is an extension that simplifies database integration in Flask applications. It provides an interface for using SQLAlchemy with Flask's application context and configuration. Learn more about Flask-SQLAlchemy: Flask-SQLAlchemy Documentation

#### Bootstrap
Bootstrap is a popular front-end framework that provides a set of pre-designed components and styles to make your web application look modern and responsive. It's built on HTML, CSS, and JavaScript and can speed up your UI development. Check out Bootstrap's official documentation: Bootstrap Documentation

#### Jinja2
Jinja2 is a template engine for Python that allows you to embed dynamic content in HTML templates. It's used in Flask applications for rendering dynamic data in HTML pages. Learn more about Jinja2: Jinja2 Documentation

#### Other Extensions
Depending on your project's requirements, you might also consider using other Flask extensions and third-party libraries to add features like user authentication, API development, and more. Always explore the Flask community and ecosystem to find extensions that fit your needs.

## Files (in progress...)
- Main.py: where the web server is run from.
- myapp (folder):
  - views.py: where most of the backend algorithms are run including the selenium web scrapper and data manipulation. 
  - models.py: where I model the data collected from the inputted link
  - database.db: where the data is stored
  - __init__.py: initializes the app and database
  - templates (folder):
    - base_table.html: where the navbar and certain table aspects are. 
    - home.html: extends base_table, where you input the link
    - table_one.html: extends base_table, where you view the data table

## Demo

Home Page and Home Page (minimized with drop-down navbar)
<img width="1429" alt="Screenshot 2023-08-10 at 11 21 23 AM" src="https://github.com/pattypic/AE_WebScrapper_Database_Flaskwebserver/assets/124921178/af17a209-81d3-4ae7-af2b-83f1654f4ede"> <img width="848" alt="Screenshot 2023-08-10 at 12 58 18 PM" src="https://github.com/pattypic/AE_WebScrapper_Database_Flaskwebserver/assets/124921178/956fb9cf-4169-4876-8097-3b30ff97a461">

Table One without data:
<img width="1426" alt="Screenshot 2023-08-10 at 11 21 42 AM" src="https://github.com/pattypic/AE_WebScrapper_Database_Flaskwebserver/assets/124921178/f2412e33-8c11-42f0-abf8-15c3ca090987">

Input Link:
<img width="1428" alt="Screenshot 2023-08-10 at 1 00 53 PM" src="https://github.com/pattypic/AE_WebScrapper_Database_Flaskwebserver/assets/124921178/29698bf3-b09f-406a-a8f4-939383e6d240">

Page Traversal view:
<img width="1440" alt="Screenshot 2023-08-10 at 1 02 47 PM" src="https://github.com/pattypic/AE_WebScrapper_Database_Flaskwebserver/assets/124921178/79a4a237-9ebb-431c-8308-1acc62f2609c">

Table One with data:

## Acknowledgment

## Roadmap
