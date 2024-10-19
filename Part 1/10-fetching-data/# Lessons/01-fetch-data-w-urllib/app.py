# Fetching Data with urllib

from urllib import request
import json
from rich import print_json

# fetching data
def get_posts():
    url = 'https://jsonplaceholder.typicode.com/posts'

    try:
        with request.urlopen(url) as response:
            data = response.read()
            return json.loads(data)
    except:
        print("could not fetch the data.")
        return None


def main():
    posts = get_posts()
    print_json(data=posts) # just to format the output


if __name__ == "__main__":
    main()
