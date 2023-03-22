### MODEL USER DB API ###
from pydantic import BaseModel

#Declaramos la entidad user
class User(BaseModel):
  id:str   # con esto "| None" indicamos que puede ser opcional
  username:str
  email:str