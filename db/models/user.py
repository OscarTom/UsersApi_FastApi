### MODEL USER DB API ###
from pydantic import BaseModel
from typing import Optional

#Declaramos la entidad user
class User(BaseModel):
  #id:str | None   # con esto "| None" indicamos que puede ser opcional
  id: Optional[str]
  username:str
  email:str