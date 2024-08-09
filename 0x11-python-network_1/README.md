
1. Fetching Internet Resources with urllib
urllib is a Python package that provides several modules for working with URLs, such as fetching data from the internet.

Fetching a Simple Web Page
python
Copy code
import urllib.request

# Fetch the contents of a URL
response = urllib.request.urlopen('https://www.example.com')
web_content = response.read()

# Print the content
print(web_content)
In this example, urllib.request.urlopen opens the URL and returns a response object. The read() method retrieves the entire content of the web page as a byte string.

2. Decoding urllib Body Response
The response body from urllib is in bytes, so you'll often need to decode it into a string format.

Decoding the Response
python
Copy code
import urllib.request

response = urllib.request.urlopen('https://www.example.com')
web_content = response.read()

# Decode the byte string to a regular string
decoded_content = web_content.decode('utf-8')
print(decoded_content)
Here, decode('utf-8') converts the byte string into a human-readable string.

3. Using the Python Package requests
requests is a popular Python library for making HTTP requests. It is more user-friendly than urllib.

Installing requests
bash
Copy code
pip install requests
Fetching a Web Page with requests
python
Copy code
import requests

# Perform a GET request
response = requests.get('https://www.example.com')

# Print the content
print(response.text)
requests.get() is used to make a GET request, and response.text returns the content of the response as a string.

4. Making HTTP GET Request
You can easily make a GET request with requests.

Example:
python
Copy code
import requests

response = requests.get('https://api.github.com')

# Print the JSON response
print(response.json())
In this case, the .json() method automatically parses the JSON response and returns a Python dictionary.

5. Making HTTP POST/PUT/etc. Requests
Other HTTP methods like POST, PUT, DELETE, etc., are also simple to use with requests.

Example: POST Request
python
Copy code
import requests

url = 'https://httpbin.org/post'
data = {'key': 'value'}

response = requests.post(url, data=data)

# Print the response
print(response.json())
This sends a POST request to the server with some data. The server responds, and the result is printed as a JSON object.

6. Fetching JSON Resources
JSON is a common format for data exchange on the web. Fetching JSON data with requests is straightforward.

Example: Fetching JSON Data
python
Copy code
import requests

response = requests.get('https://jsonplaceholder.typicode.com/posts')

# Assuming the response contains JSON data
json_data = response.json()

# Print the first item in the JSON data
print(json_data[0])
Here, we retrieve a list of posts in JSON format and print the first one.

7. Manipulating Data from an External Service
Once you've fetched data, you might want to manipulate it, such as filtering, sorting, or processing it.

Example: Filtering Data
python
Copy code
import requests

response = requests.get('https://jsonplaceholder.typicode.com/posts')
json_data = response.json()

# Filter posts by userId = 1
filtered_posts = [post for post in json_data if post['userId'] == 1]

# Print the filtered posts
for post in filtered_posts:
    print(post)
In this example, we filter posts by a specific user ID and print the results.

Conclusion
This guide covers the basics of fetching and manipulating internet resources using urllib and requests. As you progress, you can build more complex and robust applications that interact with various web services.