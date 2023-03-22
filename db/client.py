# Gestionara la conexion como cliente a mongoDb
from pymongo import MongoClient

# BBDD local
# db_client = MongoClient().local

#BBDD remota Mongo_atlas
db_client = MongoClient("mongodb+srv://test:test@cluster0.tgae9pv.mongodb.net/?retryWrites=true&w=majority").test