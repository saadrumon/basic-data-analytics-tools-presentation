import requests

url = 'https://jsonplaceholder.typicode.com/posts/1'

response = requests.get(url=url)

print(response.text)

payload = {
    "userID": "1",
    "title": "thisTitle",
    "body": "thisBody"
}

url = 'https://jsonplaceholder.typicode.com/posts'

response = requests.post(url=url, data=payload)

print(response.status_code)
print(response.text)
