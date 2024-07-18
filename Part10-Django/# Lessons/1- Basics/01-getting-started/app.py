"""
Django overview
- Django is a Python web framework that includes a set of components for solving common web development problems.
- Django allows you to rapidly develop web applications with less code by taking advantage of its framework.
- Django follows the DRY (don’t repeat yourself) principle, which allows you to maximize the code reusability.
- Django uses the MVT (Model-View-Template) pattern, which is slightly similar to MVC (Model-View-Controller) pattern.

- The MVT pattern consists of three main components:

    Model – defines the data or contains the logic that interacts with the data in the database.
    View – communicates with the database via model and transfers data to the template for representing the data.
    Template – defines the template for displaying the data in the web browser.

- Django framework itself acts as a controller. The Django framework uses URL patterns that send the request to an appropriate view.

\\\\\\\\\\\\\\\\\\\\\

- In practice, you’ll often work with models, templates, views, and URLs in the Django application.
Django architecture

- The following picture shows how Django manages HTTP request/response cycle using its components: pic-1

    The web browser requests a page by a URL and the web server passes the HTTP request to Django.
    Django matches the URL with URL patterns to find the first match.
    Django calls the view that corresponds to the matched URL.
    The view uses a model to retrieve data from the database.
    The model returns data to the view.
    The view renders a template and returns it as an HTTP response.

\\\\\\\\\\\\\\\\\\\\\\\

Creating a virtual environment

- A virtual environment creates an isolated environment that consists of an independent set of Python packages.
- By using virtual environments, you can have projects that use different versions of Django. Also, when you move the project to a different server, you can install all the dependent packages of the project using a single pip command.

- First, create a new directory django-playground:

    @@ mkdir playground

- Second, navigate to the django-playground directory:

    @@ cd playground

- Third, create a new virtual environment using the venv module:

    @@ python -m venv venv

- Fourth, activate the virtual environment:

    @@ venv\scripts\activate

- The terminal will show the following:

    ~~ (venv) D:\django-playground>

- Note that you can deactivate the virtual environment using the deactivate command:

    @@ deactivate

\\\\\\\\\\\\\\\\\\

Install the Django package

- First, issue the following pip command to install the Django package:

    @@ pip install django

- Second, check the Django version:

    @@ python -m django --version

- It’ll show something like this:

    ~~ 4.1.1

\\\\\\\\\\\\\\\\\\\\\

Exploring Django commands

- Django comes with a command-line utility program called django-admin that manages administrative tasks such as creating a new project and executing the Django development server.
- To run the Django, you execute the following command to list all Django core commands:

    @@ django-admin

- Output:

    ~~ Type 'django-admin help <subcommand>' for help on a specific subcommand.

- Available subcommands:

    [django]
        check
        compilemessages
        createcachetable
        dbshell
        diffsettings
        dumpdata
        flush
        inspectdb
        loaddata
        makemessages
        makemigrations
        migrate
        optimizemigration
        runserver
        sendtestemail
        shell
        showmigrations
        sqlflush
        sqlmigrate
        sqlsequencereset
        squashmigrations
        startapp
        startproject
        test
        testserver

- For now, we’re interested in the startproject command that creates a new Django project. The following startproject command creates a new project called django_project:

    @@ django-admin startproject django_project

- This command creates a django_project directory. Let’s explore the project structure.

    @@ cd django_project

- The following shows the django_project structure:

    ├── django_project
    | ├── asgi.py
    | ├── settings.py
    | ├── urls.py
    | ├── wsgi.py
    | └── __init__.py
    └── manage.py

- Here’s a quick overview of each file in the Django project:

    ~~ manage.py is a command-line program that you use to interact with the project like starting a development server and making changes to the database.

- The django_project is a Python package that consists of the following files:

    ~~ __init__.py – is an empty file indicating that the django_project directory is a package.
    !! settings.py – contains the project settings such as installed applications, database connections, and template directories.
    ## urls.py – stores a list of routes that map URLs to views.
    ?? wsgi.py – contains the configurations that run the project as a web server gateway interface (wsgi) application with WSGI-compatible web servers.
    @@ asgi.py – contains the configurations that run the project as an asynchronous web server gateway interface (AWSGI) application with AWSGI-compatible web servers.

\\\\\\\\\\\\\\\\\\\\\\

Running the Django development server

- Django comes with a built-in web server that allows you quickly run your Django project for development purposes.
- The Django development web server will continuously check for code changes and reloads the project automatically. However, you still need to restart the web server manually in some cases such as adding new files to the project.
- To run the Django development server, you use the runserver command:

    @@ python manage.py runserver

- Output:

    !!
      Watching for file changes with StatReloader
      Performing system checks...

      System check identified no issues (0 silenced).
      ...
      Django version 4.1.1, using settings 'django_project.settings'
      Starting development server at http://127.0.0.1:8000/
      Quit the server with CTRL-BREAK.
    !!
    
- Once the server is up and running, you can open the web app using the URL listed in the output. Typically, the URL is something like this:

    @@ http://127.0.0.1:8000/

- Now, you can copy and paste the URL to a web browser. It should show the home page

- The urls.py contains a default route that maps /admin path with the admin.site.urls view:

    from django.contrib import admin
    from django.urls import path

    urlpatterns = [
        path('admin/', admin.site.urls),
    ]

- To open the admin page, you use the following URL:

    ~~ http://127.0.0.1:8000/admin

- It’ll show a login page

\\\\\\\\\\\\\\\\\\\\\

Stop the Django development server
- To stop the Django development server, you open the terminal and press the Ctrl-C (or Command-C) twice.
Create requirements.txt file
- The requirements.txt file contains all dependencies for a specific Django project. It also contains the dependencies of dependencies.
- To create a requirements.txt file, you run the following pip command:

    @@ pip freeze > requirements.txt

- When you move the project to a new server e.g., a test or production server, you can install all the dependencies used by the current Django project using the following pip command:

    @@ pip install -r requirements.txt

\\\\\\\\\\\\\\\\\\\\\

Summary

  Django is a Python web framework that allows you to rapidly develop web applications.
  Django uses the MVT (Model-View-Template) pattern, which is similar to MVC (Model-View-Controller) pattern.
  Use the django-admin startproject new_project command to create a new project.
  Use the python manage.py runserver command to run the project using the Django development web server.
  Press Ctrl-C (or Cmd-C) to stop the Django development web server.
"""
