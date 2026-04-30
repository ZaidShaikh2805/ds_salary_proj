##import requests
##from data_input import data_in
##
##URL = 'http://127.0.0.1:5000/predict'
##headers = {"Content-Type": "application/json"}
##data = {"input": data_in}
##
##r = requests.get(URL , headers=headers, json=data)
##print("Status:", r.status_code)
##print("Text:", r.text)
##
### Only call json if valid
##if r.status_code == 200:
##    print(r.json())
##
import requests
from data_input import data_in

URL = "http://127.0.0.1:5000/predict"

r = requests.post(URL, json=data_in)

print("Status:", r.status_code)
print("Response", r.text)

if r.status_code == 200:
    print(r.json())
