''' 
	Post Request


'''


from rich import print_json
import requests


# POST requests
def save_post(data):
    url = 'https://jsonplaceholder.typicode.com/posts'

    # response = requests.post(url, data=data) # Method 1
    response = requests.post(url, json=data) # Method 2
    return response.json()


def main():
    response = save_post({
      "title": "Mario Party!",
      "body": "Okie Dokie!",
      "userId": 1
    })

    print_json(data=response)

    return


if __name__ == "__main__":
    main()
