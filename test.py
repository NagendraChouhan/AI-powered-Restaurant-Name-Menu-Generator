import requests

url = "https://router.huggingface.co/v1/models"

response = requests.get(url, timeout=20)
response.raise_for_status()

models = response.json()["data"]

for model in models:
    if "qwen" in model["id"].lower():
        print(model["id"])