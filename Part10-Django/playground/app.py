"""
DJANGO CREATE APP

## This tutorial begins where the Getting started with Django tutorial left off.

Django projects and applications

- In the Django framework:

    A project is a Django installation with some settings.
    An application is a group of models, views, templates, and URLs.

- A Django project may have one or more applications. For example, a project is like a website that may consist of several applications such as blogs, users, and wikis.
- Typically, you design a Django application that can be reusable in other Django projects. The following picture shows the structure of a Django project and its applications: pic-1

\\\\\\\\\\\\\\\\\\\\

Creating a blog application

- From previous lesson, create project 

    + install + active venv
      ~~ python -m venv venv
      ~~ venv\scripts\activate
      

    + install django + create django project
      !! pip install django  
      !! django-admin startproject django_project

    + install
      ## pip install -r requirements.txt

- To create an application, you use the startapp command as follows:
- For example, you can create an application called blog using the startapp command like this:

    @@ python manage.py startapp blog

- The command creates a blog directory with some files:

        ├── blog
        |  ├── admin.py
        |  ├── apps.py
        |  ├── migrations
        |  ├── models.py
        |  ├── tests.py
        |  ├── views.py
        |  └── __init__.py
        ├── db.sqlite3
        ├── django_project
        |  ├── asgi.py
        |  ├── settings.py
        |  ├── urls.py
        |  ├── wsgi.py
        |  ├── __init__.py
        |  └── __pycache__
        └── manage.py

\\\\\\\\\\\\\\\\\\\\\\\

Registering an application

- After creating an application, you need to register it to the project especially when the application uses templates and interacts with a database.
- The blog app has the apps.py module which contains the BlogConfig class like this:

    from django.apps import AppConfig

    class BlogConfig(AppConfig):
        default_auto_field = 'django.db.models.BigAutoField'
        name = 'blog'

- To register the blog app, you add the blog.apps.BlogConfig class to the INSTALLED_APPS list in the settings.py of the project:

    INSTALLED_APPS = [
        # ...
        'blog.apps.BlogConfig',
    ]

- Alternatively, you can use the app name like blog in the INSTALLED_APPS list like this:

    INSTALLED_APPS = [
        # ...
        'blog',
    ]

\\\\\\\\\\\\\\\\\\\\

Creating a view

- The views.py file in the blog directory comes with the following default code:

    from django.shortcuts import render

    # Create your views here.

- A view is a function that takes an HttpRequest object and returns an HttpResponse object.
- To create a new view, you import the HttpResponse from the django.http into the views.py file and define a new function that accepts an instance of the HttpRequest class:

    from django.shortcuts import render
    from django.http import HttpResponse

    def home(request):
        return HttpResponse('<h1>Blog Home</h1>')

- In this example, the home() function returns a new HttpResponse object that contains a piece of HTML code. The HTML code includes an h1 tag.
- The home() function accepts an instance of an HttpRequest object and returns an HttpResponse object. It is called a function-based view. Later, you’ll learn how to create class-based views.
- To map a URL with the home() function, you create a new file urls.py inside the blog directory and add the following code to the urls.py file:

    from django.urls import path
    from . import views

    urlpatterns = [
        path('', views.home, name='posts'),
    ]

- How it works.
  + First, import the path from django.urls module:

        from django.urls import path
  
  + Second, import the views.py module from the current directory.

        from . import views

  + Note that this is a relative import that imports the views module from the current directory.
  + Third, define a route that maps the blog URL with the home() function using the path() function.

        urlpatterns = [
            path('', views.home, name='posts'),
        ]

- The name keyword argument defines the name of the route. Later, you can reference the URL using the posts name instead of using the hard-code URL like blog/.
- By using the name for the path, you can change the URL of the path to something else like my-blog/ in the urls.py instead of changing the hard-coded URL everywhere.
- Note that the final argument of the path must be a keyword argument like name='posts'. If you use a positional argument like this:

    from django.urls import path
    from . import views

    urlpatterns = [
        path('', views.home, 'posts'), # Error
    ]

- you’ll get the following error:

    TypeError: kwargs argument must be a dict, but got str.

- To make the blog’s routes work, you need to include the urls.py of the blog application in the urls.py file of the Django project:

    from django.contrib import admin
    from django.urls import path, include

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('blog/', include('blog.urls')),
    ]

- In the urls.py of the project, we import the include function from the django.urls and map the path of the blog to the blog.urls.
- By doing this, when you navigate to http://127.0.0.1:8000/blog/, Django will run the home() function of the views.py module and returns a webpage that displays a h1 tag.
- Before opening the URL, you need to start the Django development web server:

    @@ python manage.py runserver

- When you navigate to http://127.0.0.1:8000/blog/, you’ll see a webpage that displays the Blog Home heading.
- Here’s the flow:

    First, the web browser sends an HTTP request to the URL http://127.0.0.1:8000/blog/
    Second, Django executes the urls.py in the django_project directory. It matches the blog/ with the URL in the urlpatterns list in the urls.py. As a result, it sends '' to the urls.py of the blog app.
    Third, Django runs the urls.py file in the blog application. It matches the '' URL with the views.home function and execute it, which returns an HTTP response that outputs a h1 tag.
    Finally, Django returns a webpage to the web browser.

\\\\\\\\\\\\\\\\\\\

Adding more routes
- First, define the about() function in the views.py of the blog application:

    from django.shortcuts import render
    from django.http import HttpResponse

    def home(request):
        return HttpResponse('<h1>Blog Home</h1>')


    def about(request):
        return HttpResponse('<h1>About</h1>')

- Second, add a route to the urls.py file:

    from django.urls import path
    from . import views

    urlpatterns = [
        path('', views.home, name='posts'),
        path('about/', views.about, name='about'),
    ]

- Third, open the URL http://127.0.0.1:8000/blog/about/, and you’ll see a page that displays the about page.
- Now, if you open the home URL, you’ll see a page that displays a page not found with a 404 HTTP status code.
- The reason is that the urls.py in the django_project doesn’t have any route that maps the home URL with a view.
- To make the blog application the homepage, you can change the route from blog/ to '' as follows:

    from django.contrib import admin
    from django.urls import path, include


    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include('blog.urls')),
    ]

- If you open the URL http://127.0.0.1:8000, you’ll see the blog home page. And navigating to the URL http://127.0.0.1:8000/about/ will take you to the about page.

\\\\\\\\\\\\\\\\\\\

Summary

  A Django project contains one or more applications.
  A Django application is a group of models, views, templates, and URLs.
  Use python manage.py startapp app_name command to create a new Django application.
  Define a function in the views.py file to create a function-based view.
  Define a route in the urls.py file of the application to map a URL pattern with a view function.
  Use the include() function to include the urls.py of app in the urls.py of the project.


"""
