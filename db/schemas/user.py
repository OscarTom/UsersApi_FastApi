
""" Esta funcion transforma la respuesta de la BBDD que viene en un json
al objeto User con el que estamos trabajando. Igualamos cada propiedad de nuestro objeto 
con la que viene en la BBDD"""

def user_schema(user) -> dict:
  return {
    "id": str(user["_id"]),
    "username": user["username"],
    "email": user["email"]
  }
  
def users_schema(users) -> list:
  lista = []
  for user in users:
    lista.append(user_schema(user))
  return lista    #[user_schema(user) for user in users]