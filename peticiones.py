import requests

url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url)

if response.status_code == 200 :
    print("La solicitud fue exitosa")
    ususario = response.json()
    print(f"Nombre: {ususario[0]['name']}")
    

