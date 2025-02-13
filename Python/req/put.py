import requests

response = requests.put("https://httpbin.org/put",data={'key' :'value'})
print(response.status_code)
print(response.content)