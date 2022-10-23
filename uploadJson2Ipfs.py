


import requests
import json

f = open('config.json')
data = json.load(f)

print(data['IPFS_projectID'])

projectID = data['IPFS_projectID']
secretKey = data['IPFS_secretKey']

def upload_json(JsonFile):
    f = open(JsonFile)
    json_data = json.load(f)

    files = {
        'file': str(json_data),
    }
    response = requests.post('https://ipfs.infura.io:5001/api/v0/add', files=files, auth=(projectID,secretKey))
    if response.status_code == 200:
        print ('Upload IPFS successful')
        return response.json()["Hash"]
    else:
        return False

print(upload_json('review.json'))