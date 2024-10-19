'''
  Virtual Environment
  - python -m venv .venv
    -> venv: convention
  - .\.venv\Scripts\activate
    -> activate virtual environment
  - deactivate
  - pip list
    -> can run in virtual environment or globally


************************

  Install Packages in Virtual Environment
  - active virtual environment
  - pip install rich
  - pip list
  - python -m rich
  - Python: Selective Interpreter -> Enter Interpreter Path


************************

  pip freeze & requirements.txt
  - User A:
    # pip freeze > requirements.txt
    # upload to github -> we don't want to upload .venv 
  - User B: 
    # python -m venv .venv
    # .\.venv\Scripts\activate
    # pip install -r requirements.txt
    # Select Interpreter -> Enter Interpreter Path -> Script/python.exe


'''

from rich import print


def main():
    print("Hello, [underline red]Ninjas[/]!")
    return


if __name__ == "__main__":
    main()
