from pathlib import Path
import json # standard library


path = Path(__file__).parent / 'characters.json'


characters = {
  "characters": [
    {"name": "Mario", "age": 25},
    {"name": "Luigi", "age": 27},
    {"name": "Peach", "age": 26},
    {"name": "Bowser", "age": 35}
  ]
}


def write_json():
  with path.open('w') as file:
    # dump/write data into file -> json.dump()
    json.dump(characters, file, indent=2) # indent=2 -> format
  return


def read_json():
  with path.open('r') as file:
    # read/decoding data from json file -> json.load()
    data = json.load(file)
  return data


def main():
  write_json()
  data = read_json()
  print(data)


if __name__ == "__main__":
  main()