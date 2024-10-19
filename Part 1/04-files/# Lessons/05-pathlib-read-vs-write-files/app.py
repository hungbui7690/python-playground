# open characters.txt 

from pathlib import Path


def create_path():
  script_dir = Path(__file__).parent
  path = script_dir / 'characters' # create file path
  path.mkdir(parents=True, exist_ok=True) # create dir
  path = path / 'zelda.txt'
  path.touch(exist_ok=True) # create file

  # file = path.open('w')
  # file.write("Ganon")

  # file = path.open('a')
  # file.write('\nLink')

  file = path.open('r')
  content = file.read()
  print(content)

  file.close()

  # convenience method for writing
  path.write_text('Epona')

  # convenience method for reading
  content = path.read_text()
  print(content)

  return

def main():
  create_path()

if __name__ == "__main__":
  main()