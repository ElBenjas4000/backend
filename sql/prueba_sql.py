import requests

def crear_usuario(id, nombre):
    r = requests.post("http://127.0.0.1:8000/crear_usuario", json={
        "id": id,
        "name": nombre
    })
    print(r.json())

def obtener_usuarios():
    r = requests.get("http://127.0.0.1:8000/usuarios")
    return r.json()