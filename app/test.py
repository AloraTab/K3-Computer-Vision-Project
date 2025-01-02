import requests

url = "http://0.0.0.0:80/predict/"
files = {"file": open("img/test-img.jpg", "rb")}
response = requests.post(url, files=files)
print(response.json())
