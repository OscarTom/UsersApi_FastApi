### USER DB API ###
from fastapi import HTTPException, FastAPI, status
from db.models.user import User
from db.client import db_client
from db.schemas.user import user_schema, users_schema
from bson import ObjectId


app = FastAPI()

#Iniciar el servidor: uvicorn main:app --reload
#Url local: http://localhost:8000/users



############ GET ###################
# Llamamos a traves de la url al get y nos devuelve toda la lista de usuarios
@app.get("/usersdb")
async def users():
  """users = db_client.users.find()
  users = users_schema(users)
  return users"""
  return users_schema(db_client.users.find())

# PATH --> Devolver un usuario con parametros http://localhost:8000/user/2
@app.get("/userdb/{id}")
async def userId(id: str):
  return search_user("_id",ObjectId(id))
  
  
# QUERY --> Devolver un usuario con query  http://localhost:8000/userquery/?id=2
@app.get("/userdb/")
async def userId(id: str):
  return search_user("_id",ObjectId(id))

  
############ POST ###################
@app.post("/userdb/", response_model=User, status_code=201)
async def user(user: User):
  if type(search_user("email",user.email)) == User: 
    raise HTTPException(status_code=404,detail="El usuario ya existe")
  
  #Tranformamos el modelo usuario en un diccionario
  user_dict = dict(user)
  del user_dict["id"]
  
  # Inserta el usuario en la BBDD y nos quedamos con el id asignado
  id = db_client.users.insert_one(user_dict).inserted_id
  # Busca en la BBDD y nos devuelve un json con los datos
  new_user = db_client.users.find_one({"_id":id})
  # LLamamos a la funcion que nos convierte de json a nuestro shema de User
  new_user = user_schema(new_user)
  
  return User(**new_user)
  
############ PUT ###################
@app.put("/userdb/", response_model=User)
async def user(user : User):
  user_dict = dict(user)
  del user_dict["id"]

  
  try:
    db_client.users.find_one_and_replace({"_id":ObjectId(user.id)}, user_dict)
  except:
    return {"error":"No se ha actualizado el usuario."}
    
  return search_user("_id", ObjectId(user.id))
  
  
############ DELETE ###################
@app.delete("/userdb/{id}")
async def user(id: str):
  # Buscamos el usuario en la BBDD 
  found = db_client.users.find_one_and_delete({"_id":ObjectId(id)})
  return {"ok":"Usuario eliminado correctamente."}
  if not found:
    return {"error":"No se ha eliminado el usuario."}
      
def search_user(field: str, key):
  
  try:
    user = db_client.users.find_one({field:key}) #buscamos el usuario por email
    user = user_schema(user) #Aplicamos el esquema al usuario encontrado
    return User(**user) #Lo retornamos como un objeto User
  except:
    return {"error":"El usuario NO existe en la base de datos."}