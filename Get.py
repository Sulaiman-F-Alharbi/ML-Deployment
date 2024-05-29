import requests
url = "http://localhost:8000/predict"
params = {
    "Year": 2020,
    "Engine_Size": 2.5,
    "Mileage": 15000,
    "Type": "Accent",
    "Make": "Hyundai",
    "Options": "Full"
}
response = requests.get(url, params=params)
print(response.json())


import requests
url = "http://localhost:8000/predict"
data = {
    "Year": 2020,
    "Engine_Size": 2.5,
    "Mileage": 15000,
    "Type": "Accent",
    "Make": "Hyundai",
    "Options": "Full"
}
response = requests.post(url, json=data)
print(response.json())