import requests

API_URL = "http://127.0.0.1:8000/predict"
input_data = {
    "age": 30,
    "weight": 70.0,
    "height": 1.75,
    "income_lpa": 10.0,
    "smoker": False,
    "city": "Mumbai",
    "occupation": "private_job"
}

response = requests.post(API_URL, json=input_data)
print(response.json())  # Should show the prediction result
