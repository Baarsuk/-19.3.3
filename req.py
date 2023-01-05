import requests
import json

input_pet = {
    "id": 727,
    "category": {
        "id": 7,
        "name": "DOl"
    },
    "name": "doggie",
    "photoUrls": [
        "string"
    ],
    "tags": [
        {
            "id": 2,
            "name": "dog"
        }
    ],
    "status": "available"
}
headers = {
    'accept': 'application/json',
    'Content-Type': 'application/json'
}


res_post = requests.post(url='https://petstore.swagger.io/v2/pet',
                         json=input_pet,
                         # data=json.dumps(input_pet),
                         headers=headers)

print()
print('создали нового пета')
print(res_post.status_code)
print(res_post.text)


headers = {
    'accept': 'application/json',
    'Content-Type': 'multipart/form-data'
}

image = open('xbadger.jpg', 'rb')
file = {'file': image, 'type': 'image/jpeg'}
res_post = requests.post(url=f'https://petstore.swagger.io/v2/pet/{input_pet["id"]}/uploadImage',
                     headers=headers,
                     data=file)

print()
print('добавили фотографию')
print(res_post.status_code)
print(res_post.text)




input_pet = {
    "id": 727,
    "category": {
        "id": 12,
        "name": "Boris"
    },
    "name": "doggie",
    "photoUrls": [
        "string"
    ],
    "tags": [
        {
            "id": 2,
            "name": "cat"
        }
    ],
    "status": "available"
}

res_put = requests.put(url='https://petstore.swagger.io/v2/pet',
                       data=json.dumps(input_pet),
                       headers=headers)

print()
print('меняем данные у пета')
print(res_put.status_code)
print(res_put.text)


status = 'sold'
headers = {
    'accept': 'application/json',
    'Content-Type': 'application/x-www-form-urlencoded'
}

res_post = requests.post(url=f'https://petstore.swagger.io/v2/pet/{input_pet["id"]}',
                         headers=headers,
                         data={'status': {status}})

print()
print('меняем статус Пета')
print(res_post.status_code)
print(res_post.text)


res_get = requests.get(url=f'https://petstore.swagger.io/v2/pet/{input_pet["id"]}')

print()
print('проверяем, что статус изменился')
print(res_get.status_code)
print(res_get.text)


res_delete = requests.delete(url=f'https://petstore.swagger.io/v2/pet/{input_pet["id"]}')

print()
print('удаляем Пета')
print(res_delete.status_code)
print(res_delete.text)


res_get = requests.get(url=f'https://petstore.swagger.io/v2/pet/{input_pet["id"]}')

print()
print('проверяем, что пет удален')
print(res_get.status_code)
print(res_get.text)


status = 'available'
headers = {'accept': 'application/json'}

res_get = requests.get(url=f'https://petstore.swagger.io/v2/pet/findByStatus?status={status}', headers=headers)

print()
print('findByStatus')
print(res_get.status_code)
print(res_get.text)