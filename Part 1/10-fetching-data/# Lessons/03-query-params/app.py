''' 
	Adding Query Parameters
  - Filtering resources by a query parameter
	- Method 1: /posts?userId=1
	- Method 2: params={'userId': 1}
		-> we will use this method


'''


from rich import print_json

import requests


# fetching data
def get_posts(user_id=1):
    url = 'https://jsonplaceholder.typicode.com/posts'

    #
    params = {
      "userId": user_id
    }

    response = requests.get(url, params=params) #
    parsed_json = response.json()

    return parsed_json


def main():
    posts = get_posts()
    print_json(data=posts)


if __name__ == "__main__":
    main()
