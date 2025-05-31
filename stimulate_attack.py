import requests

url = "http://FlaskAppALB-1437984442.eu-north-1.elb.amazonaws.com/login"  # Add http://
data = {"username": "admin", "password": "wrongpass"}

for i in range(10):
    response = requests.post(url, data=data)
    print(f"[{i}] Status: {response.status_code}")
