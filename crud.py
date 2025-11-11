import json, os
import main

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
json_path = os.path.join(BASE_DIR, "estudiante.json")


class DataBase():
    def __init__(self):
        self.archivo = json_path
        with open(self.archivo, 'r') as file:
            self.datos = json.load(file)
    

    def create(self, name, dato):
        if os.path.exists(self.archivo):
            with open(self.archivo, "r", encoding="utf-8") as f:
                datos = json.load(f)   
        else:
            datos = {}

        datos[name] = dato

        with open(self.archivo, "w", encoding="utf-8") as f:
            json.dump(datos, f, indent=4, ensure_ascii=False)


    def read(self):
        return self.datos
        
    def update(self):
        with open(self.archivo, "w", encoding="utf-8") as f:
            json.dump(self.datos, f, indent=2, ensure_ascii=False)
        
    def delete(self, dato):
        if dato in self.datos:
            del self.datos[dato]
            
        self.update()
        




