import requests

response = requests.delete("https://httpbin.org/delete",data={'key' :'value'})
print(response.status_code)
print(response.content)