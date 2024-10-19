# Fetching Data with Requests

from rich import print_json
import requests


# fetching data
def get_posts():
    url = 'https://jsonplaceholder.typicode.com/posts'

    response = requests.get(url)
    return response.json()


def main():
    posts = get_posts()
    print_json(data=posts)


if __name__ == "__main__":
    main()
