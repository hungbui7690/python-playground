"""
INSTALL PIPENV WINDOWS

\\\\\\\\\\\\\\\\\\\\\\\\

Prerequisites

- Before installing the pipenv tool, you need to have Python and pip installed on your computer.

- First, open the Command Prompt or Windows Powershell and type the following command.

    ~~ python -V

- Note that the letter V in the -V is uppercase. If you see the Python version like the following:

    Python 3.8.5

- …then you already have Python installed on your computer. Otherwise, you need to install Python first.
- Second, use the following command to check if you have the pip tool on your computer:

    ~~ pip -V

- It’ll return something like this:

    pip 20.2.4 from C:\\Users\\<username>\AppData\Roaming\Python\Python38\site-packages\pip (python 3.8)

\\\\\\\\\\\\\\\\\\\\\\\\

Install pipenv on Windows

- First, use the following command to install pipenv tool:

    ~~ pip install pipenv

- Second, replace your <username> in the following paths and add them to the PATH environment variable:

    c:\\Users\<username>\AppData\Roaming\Python\Python38\Site-Packages
    C:\\Users\<username>\AppData\Roaming\Python\Python38\Scripts

- It’s important to notice that after changing the PATH environment variable, you need to close the Command Prompt and reopen it.

- Third, type the following command to check if the pipenv installed correctly:

    ~~ pipenv -h

- If it shows the following output, then you’ve successfully installed the pipenv tool successfully.

    ~~ Usage: pipenv [OPTIONS] COMMAND [ARGS]...
        ...

- However, if you see the following message:

    pipenv shell 'pipenv' is not recognized as an internal or external command, operable program or batch file.

- Then you should check step 2 to see if you have already added the paths to the PATH environment variable.

- In this tutorial, you have learned how to install the pipenv tool on Windows computers.


"""

#
