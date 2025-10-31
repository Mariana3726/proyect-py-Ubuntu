import requests

def get_razas():
    r = requests.get('https://dog.ceo/api/breeds/list')
    print(r.status_code)
    #print(r.text)
    print(type(r.text)) #en este caso es un string por el text
    #pero encontramos un diccionario con listas
    razas = r.json()
    for raza in razas.values(): #utilizamos la función para ver los valores del diccionario
        print(f"Raza de perros: {raza[5]}")
