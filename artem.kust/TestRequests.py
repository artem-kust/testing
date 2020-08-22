import requests

# URI
uri = "http://localhost:5002/"

# Send GET Request to the Server
GetResponse = requests.get(uri, headers={'Content-Type': 'application/JSON'})
print(GetResponse)

# Send GET Request to the Server to get headers
GetHeaders = requests.get('http://localhost:5002/headers', headers={'Content-Type': 'application/JSON'})
print(GetHeaders.headers)

# Send POST request to log in under test credentials
session = requests.Session()
session.post('http://localhost:5002/login', {'username': 'test', 'password': 'test', })

# Send POST Request to the Server
PostResponse = requests.post(uri, headers={'Content-Type': 'application/JSON'}, json={'just for testing': 'Just for testing'})
print(PostResponse)

# Send PUT Request to the Server. This method is not allowed on the server, so just to test it.
PutResponse = requests.put(uri, headers={'Content-Type': 'application/JSON'}, json={'Testing': 'Testing'})
if PutResponse.status_code == 405:
    print('The PUT method is not allowed on the server.')
elif PutResponse.status_code == 404:
    print('An error occurred.')

#

