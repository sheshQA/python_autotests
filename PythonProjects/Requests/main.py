import requests

url_pet = 'https://petstore.swagger.io/v2/pet'
response=requests.post(url_pet, json={
  "id": 8,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "ovi",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
})
print(response.text)

response=requests.put(url_pet, json={
  "id": 8,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "kuch",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
})
print(response.text)

response=requests.get('https://petstore.swagger.io/v2/pet/8')
print(response.text)
print(response.status_code)