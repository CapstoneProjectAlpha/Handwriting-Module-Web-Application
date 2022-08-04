import requests
import json 

url = ""
KEY = ""

def fetchResults(file):    
    with open(f'./{file}', 'rb') as f:
        data = f.read()
    headers = {
    'Ocp-Apim-Subscription-Key': KEY,
    'Content-Type': 'image/png'
    }
    response = requests.request("POST", url, headers=headers, data=data)
    location = response.headers['Operation-Location']
    headers = {
    'Ocp-Apim-Subscription-Key': KEY
    }
    response = requests.request("GET", location, headers=headers)
    final_data = json.loads(response.text)
    set_of_words_found = []
    for elem in final_data['analyzeResult']['readResults']:
        for el in elem["lines"]:
            set_of_words_found.append(el["text"])
    return set_of_words_found

