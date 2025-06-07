# Overview

The Recipe Finder web application is designed to enhance my skills as a software engineer by building a dynamic, interactive web app using Django and Python. The app allows users to maintain a personal pantry of ingredients, which can be used to search for matching recipes from a database populated via an external API. The goal is to create a practical, user-friendly tool that integrates backend data management with a clean frontend interface.

To start the app locally, run the Django development server with the command:
- python manage.py runserver

Then open your web browser and navigate to:
- http://127.0.0.1:8000/

Here you will find the home page where you can manage your pantry ingredients and search recipes based on those items. After clicking a button on the home page, it will take you the the second page which is dynamically made to show the matched recipes with the ingredients in the pantry from the home page.

The purpose of this software is to practice full-stack web development concepts, including database modeling, API integration, form handling, URL routing, and dynamic templating with Django.

[Software Demo Video](https://youtu.be/wIaXVyaJ7cw)


# Web Pages

The app contains two main web pages:
* Home Page (/): This page displays the user’s pantry where they can add or delete ingredients. It dynamically renders the pantry items stored in the database and provides a button to search for recipes using the pantry contents.
* Results Page (/results/): After initiating a search, this page shows recipes matching the pantry ingredients. Each recipe is dynamically generated with its name, image (if available), ingredients list, and a toggleable section to show/hide cooking instructions.

Navigation is handled through standard HTTP GET requests, with forms on the home page redirecting to the results page with query parameters.


# Development Environment

Tools Used: 
* Visual Studio Code for coding
* Git for version control
* Django’s built-in development server for local testing

Programming Languages:
* Python for backend development using the Django web framework
* HTML and CSS for web page structure and styling

Libraries and APIs:
* Django (version 5.2.2) for web framework and ORM
* 'requests' library to call the Spoonacular API for fetching recipes
* Spoonacular API for obtaining recipe data


# Useful Websites

* [Django Documentation and Tutorial](https://docs.djangoproject.com/en/5.2/)
* [Django Tutorial—TutorialsPoint](https://www.tutorialspoint.com/django/index.htm)
* [Django Tutorial—RealPython](https://realpython.com/get-started-with-django-1/)
* [ChatGPT](https://chatgpt.com/)


# Future Work

* Improve the recipe matching algorithm to rank and display results based on ingredient closeness
* Implement user authentication to save personal pantries per user
* Add pagination and filtering options on the results page for better usability
* Enhance frontend UI with responsive design and accessibility improvements
* Cache API calls or maintain a scheduled update to reduce repeated external requests