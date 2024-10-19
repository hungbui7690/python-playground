# pathlib module: https://docs.python.org/3/library/pathlib.html
from pathlib import Path

# print(Path(__file__)) # 04-files\playground\app.py
# print(Path(__file__).parent) # 04-files\playground
# print(Path.cwd()) # 04-files


def create_path():
  # create file path
  path = Path(__file__).parent  / 'characters'
  print(path) # 04-files\playground\characters

  # create dir from the path above
  path.mkdir(parents=True, exist_ok=True) 

  return


def main(): 
  create_path()


if __name__ == "__main__":
  main()