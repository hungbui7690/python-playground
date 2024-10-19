"""
CREATING A NEW PROJECT

- First, create a new project folder e.g., crawler.

- Second, navigate to the crawler folder and install the requests package using the pipenv command:

    ~~ pipenv install requests

- Output:

    Creating a Pipfile for this project…
    Installing requests…
    Adding requests to Pipfile's [packages]…
    Installation Succeeded
    Pipfile.lock not found, creating…
    Locking [dev-packages] dependencies…
    Locking [packages] dependencies…
    Locking...Building requirements...
    Resolving dependencies...
    Success!
    Updated Pipfile.lock (fbd99e)!
    Installing dependencies from Pipfile.lock (fbd99e)…
    ================================ 0/0 - 00:00:00

    Successfully created virtual environment!
    Virtualenv location: C:\\Users\<username>\.virtualenvs\playground-a67ssGAy

@@ And you’ll see that pipenv created two new files called Pipfile and Pipfile.lock. On top of that, it installed a virtual environment.

- If you look at the project folder, you won’t see the virtual environment folder.
@@ We can see that the VirtualEnv location is in a different folder (unlike venv.)

- To find the location of the virtual environment, you use the following command:

    ~~ pipenv --venv

- It’ll return something like this on Windows:

    C:\\Users\<username>\.virtualenvs\playground-a67ssGAy

- Note that the <username> is the username that you use to log in to Windows.

- Third, create a new file called app.py in the project folder and add the following code to the file:

    @@
        import requests
        response = requests.get('https://www.python.org/')
        print(response.status_code)
        Code language: JavaScript (javascript)
    @@

- In this code, we imported the requests third-party module, use the get() function to make an HTTP request to the URL https://www.python.org/ and display the status code (200).

- Fourth, run the app.py file from the terminal by using the python command:

    ~~ python app.py

- It’ll show the following error:

    ModuleNotFoundError: No module named 'requests'

- The reason is that Python couldn’t locate the new virtual environment. To fix this, you need to activate the virtual environment.

- Fifth, use the following command to activate the new virtual environment:

    ~~ pipenv shell

    @@ we will see the label that notifies us on the right side of the terminal

- If you run the app.py now, it should work correctly:

    ~~ python app.py

- Output:

    200

- The status code 200 means the HTTP request has succeeded.

- Sixth, use the exit command to deactivate the virtual environment:

    ~~ exit

\\\\\\\\\\\\\\\\\\\\\

Install Packages from Pipfile
- The proper answer to this question is that 
    ~~ pipenv install 
or 
    ~~ pipenv install --dev 
(if there are dev dependencies) should be ran. 

- That will install all the dependencies in the Pipfile. Putting the dependencies into a requirements.txt and then using pip will work but is not really necessary. 
- The whole point of using pipenv for most people is to avoid the need to manage a requirements.txt or to use pip.

NOTE: if the <virtualenv> is already activated, you can also use 
    @@ pipenv sync 
or 
    @@ pipenv sync --dev 
for the same effect.

\\\\\\\\\\\\\\\\\\\\

Requirements File

- https://fig.io/manual/pipenv/sync
- Ideally, you are encouraged to have a requirements.txt file which contains all the packages required for installation via pip. You can create this file by doing:

    ?? pip freeze > requirements.txt

- You can convert a Pipfile and Pipfile.lock into a requirements.txt.

    ?? pipenv lock -r > requirements.txt

- After that, you can install all your modules in your python virtual environment by doing the following:

    ?? pip install -r requirements.txt

NOTE: Make sure to update the "requirements.txt" file by using "pip freeze"

"""

import requests

response = requests.get("https://www.python.org/")
print(response.status_code)
