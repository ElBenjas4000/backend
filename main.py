import crud 
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
listUsers = []
database = crud.DataBase()

@app.get("/")
async def index():
    return {"mensaje":"Hello word"}

@app.post("/crear_usuario")
def usuario(name, id):
    database.create(id, name)

@app.post("/enviar_usuario")
async def recibir_json(request: Request):
    data = await request.json()
    print("Datos recibidos:", data)
    
    name = data.get("name")
    id = data.get("id")
    
    database.create(id, name)

@app.get("/cargar_usuario") 
def usuarios():
    return {"Los usuarios son:": database.read()}


