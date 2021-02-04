import requests
import html

response = requests.get(url="https://opentdb.com/api.php?amount=10&type=boolean")
question_data = response.json()["results"]

for i in question_data:
    i["question"] = html.unescape(i["question"])

