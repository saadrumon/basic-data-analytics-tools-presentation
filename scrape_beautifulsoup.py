from bs4 import BeautifulSoup


html_doc = """
<html>
  <head>
    <title>Example HTML Document</title>
  </head>
  <body>
    <p class="title">Example paragraph!</p>
    <a href="https://jsonplaceholder.typicode.com/posts/1">Link 1</a>
    <a href="https://jsonplaceholder.typicode.com/posts/2">Link 2</a>
  </body>
</html>
"""

soup = BeautifulSoup(html_doc, 'lxml')

print(soup.title)
# output: <title>Example HTML Document</title>

print(soup.find_all('a')[0]['href'])
# output: https://jsonplaceholder.typicode.com/posts/1
