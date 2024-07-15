"""
\\\\\\\\\\\\\\\\\\

What is a Python virtual environment

- Python uses virtual environments to create an isolated environment for every project. In other words, each project will have its own directory to store third-party packages.
- In case you have multiple projects that use different versions of a package, you can store them in separate virtual environments.
- Python includes the virtual environment module (venv) as a standard library since version 3.3. Therefore, to use the venv module, you should have Python 3.3 or later.

- To check the Python’s version, you can use the following command:

    python --version

\\\\\\\\\\\\\\\\\\

Using the venv module to create a virtual environment

- The following example shows you how to create a new project on Windows, which uses a virtual environment created by the venv built-in module.
- First, create a new folder for hosting the project and virtual environment:

    ~~ mkdir D:\test_env
    ~~ cd test_env

- Second, create a virtual environment with the name project_env inside the test_env folder:

    ~~ python -m venv project_env

- The above command will create a new folder called project_env with all necessary tools and libraries for running Python programs.
- Use the following command to check where the python.exe is located:

    ~~ where python

- It’ll return the following path indicating that the python.exe is located in the installation folder:

    C:\Python\python.exe

- Second, activate the virtual environment by running the activate.bat file in the project_env/Scripts directory:

    ~~ project_env\Scripts\activate

- Once executed, you’ll see the following in the terminal:

    ~~ (project_env) D:\test_env\project_env\Scripts>

- The prefix (project_env) indicates that you’re in the project_env virtual environment.
- Now, you can check where the python.exe is located again:

    ~~ where python

- This time it returns the following paths:

    D:\test_env\project_env\Scripts\python.exe
    C:\Python\python.exe

- The first line shows that the python.exe is located in the project_env/Scripts folder. It means that if you run the python command within the project_env, the D:\test_env\project_env\Scripts\python.exe will execute instead of C:\Python\python.exe.

- Third, navigate to the D:\test_env, create a new project folder called web_crawler, and navigate to the web_crawler folder:

    cd..
    cd..
    mkdir web_crawler
    cd web_crawler

- Fourth, show the packages installed in the project_env virtual environment for the web_crawler project:

    ~~ pip list

- Output: just 2 packages

    Package    Version
    ---------- -------
    pip        22.0.4
    setuptools 58.1.0

- When you created the project_env virtual environment, the venv module already installed two packages: pip and setuptools.

- Fifth, install the requests package in the virtual environment:

    ~~ pip install requests

- If you display all packages installed in the project_env virtual environment (pip list), you’ll see the requests package and its dependencies:

    Package            Version
    ------------------ ---------
    certifi            2022.9.24
    charset-normalizer 2.1.1
    idna               3.4
    pip                22.0.4
    requests           2.28.1
    setuptools         58.1.0
    urllib3            1.26.12

- Sixth, create the requirements.txt file:
    + Output installed packages in requirements format.
    + packages are listed in a case-insensitive sorted order.

    ~~ pip freeze > requirements.txt

- The content of the requirements.txt will look like this:

    certifi==2022.9.24
    charset-normalizer==2.1.1
    idna==3.4
    requests==2.28.1
    urllib3==1.26.12

- The requirements.txt file contains all the packages with versions installed in the project_env virtual environment used for the project.
- When you copy the project to a different machine, you can run the pip install command to install all the packages listed in the requirements.txt file.

- Seventh, create the main.py file that uses the requests module:
    @@
        import requests
        response = requests.get('https://www.google.com')
        if response.status_code == 200:
            print(response.text)
    @@

- To run the main.py file, you can use the python command as usual:

    ~~ python main.py

- This command executes the python.exe from the project_env and loads the packages installed in the project_env virtual environment.
- To deactivate the virtual environment, you can run the deactivate command:

    ~~ deactivate

- It’ll return the following:

    D:\test_env\web_crawler>

- Now, you don’t see the (project_env) prefix anymore. It means that you’re not in the project_env virtual environment.


\\\\\\\\\\\\\\\\\\

Share Project to Another Machine 

    1. delete project_env folder
    2. share project
    3. create virtual environment 
        > python -m venv project_env
        > .\activate
    4. pip install -r ..\\..\\web-crawler\\requirements.txt
        > -r: install from requirement file 


\\\\\\\\\\\\\\\\\\

Summary

- A virtual environment creates an isolated environment for a Python project.
- Use the venv module to create a new virtual environment.

"""
