from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from crud_sql import DataBase

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

database = DataBase()

@app.get("/")
def index():
    return {"mensaje": "API con SQLite funcionando"}

# Crear usuario
@app.post("/crear_usuario")
async def crear_usuario(request: Request):
    data = await request.json()
    name = data.get("name")
    user_id = data.get("id")

    ok, msg = database.create(user_id, name)
    return {"success": ok, "message": msg}

# Leer todos
@app.get("/usuarios")
def obtener_usuarios():
    usuarios = database.read_all()
    return [{"id": u[0], "name": u[1]} for u in usuarios]

# Leer uno
@app.get("/usuario/{user_id}")
def obtener_usuario(user_id: str):
    user = database.read_one(user_id)
    if user:
        return {"id": user_id, "name": user[0]}
    return {"error": "Usuario no encontrado"}

# Actualizar
@app.put("/actualizar_usuario")
async def actualizar_usuario(request: Request):
    data = await request.json()
    user_id = data.get("id")
    new_name = data.get("name")

    updated = database.update(user_id, new_name)
    return {"updated": updated > 0}

# Eliminar
@app.delete("/eliminar_usuario/{user_id}")
def eliminar_usuario(user_id: str):
    deleted = database.delete(user_id)
    return {"deleted": deleted > 0}
