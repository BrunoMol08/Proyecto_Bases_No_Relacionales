"""
Script que realiza la inserción de la información dentro de la base de datos.
"""

#Librerias importadas 
import requests
import pymongo
from pymongo import MongoClient

client = "mongodb://mongo-apilegislativo:tDvheHSP8lTpsJ0brhOAhL5AcYSJADcTSFV5w3u7tW1ILFWJFFbYtZ35xJuIsfOKApasyKL2p8pxj1HZHN8nag==@mongo-apilegislativo.mongo.cosmos.azure.com:10255/?ssl=true&retrywrites=false&replicaSet=globaldb&maxIdleTimeMS=120000&appName=@mongo-apilegislativo@"

#Eliminamos la base de datos apilegislativo, en caso de existir
myclient = pymongo.MongoClient(client)
myclient.drop_database("apilegislativo")

#Inserción de la información de de la base de datos 
with open('/home/bruno/Documentos/Bases_no_relacionales/conf/token_api.txt') as f:
    var = f.read()
authorization = var

payload={}
headers = {
    'Authorization': authorization
}

#Importación a MongoDB Iniciativas aprobadas

url = "https://api.apilegislativo.com/iniciativa/aprobada/"


response = requests.request("GET", url, headers=headers, data=payload)

myclient = pymongo.MongoClient(client) # similar a ejecutar mongosh
mydb = myclient["apilegislativo"] # == use apilegislativo
mycol = mydb["iniciativasaprobadas"] # == db.iniciativasaprobadas...
iniciativas = response.json()
x = mycol.insert_many(iniciativas["iniciativas"]) # find({"iniciativas:{$exists:true}"})

#Importación a MongoDB Iniciativas desechadas
url = "https://api.apilegislativo.com/iniciativa/desechada/"

response = requests.request("GET", url, headers=headers, data=payload)

myclient = pymongo.MongoClient(client) # similar a ejecutar mongosh
mydb = myclient["apilegislativo"] # == use apilegislativo
mycol = mydb["iniciativasdesechadas"] # == db.iniciativasaprobadas...
iniciativas = response.json()
x = mycol.insert_many(iniciativas["iniciativas"]) 

#Importación a MongoDB Iniciativas por partido PAN
url = "https://api.apilegislativo.com/iniciativa/partido/pan"

response = requests.request("GET", url, headers=headers, data=payload)

myclient = pymongo.MongoClient(client) # similar a ejecutar mongosh
mydb = myclient["apilegislativo"] # == use apilegislativo
mycol = mydb["PAN"] # == db.iniciativasaprobadas...
iniciativas = response.json()
x = mycol.insert_many(iniciativas["iniciativas"])

#Importación a MongoDB Iniciativas por partido PRI
url = "https://api.apilegislativo.com/iniciativa/partido/pri"

response = requests.request("GET", url, headers=headers, data=payload)

myclient = pymongo.MongoClient(client) # similar a ejecutar mongosh
mydb = myclient["apilegislativo"] # == use apilegislativo
mycol = mydb["PRI"] # == db.iniciativasaprobadas...
iniciativas = response.json()
x = mycol.insert_many(iniciativas["iniciativas"]) 

#Importación a MongoDB Iniciativas por partido MORENA
url = "https://api.apilegislativo.com/iniciativa/partido/morena"

response = requests.request("GET", url, headers=headers, data=payload)

myclient = pymongo.MongoClient(client) # similar a ejecutar mongosh
mydb = myclient["apilegislativo"] # == use apilegislativo
mycol = mydb["MORENA"] # == db.iniciativasaprobadas...
iniciativas = response.json()
x = mycol.insert_many(iniciativas["iniciativas"]) 

#Importación a MongoDB Iniciativas por partido PRD
url = "https://api.apilegislativo.com/iniciativa/partido/PRD"

response = requests.request("GET", url, headers=headers, data=payload)

myclient = pymongo.MongoClient(client) # similar a ejecutar mongosh
mydb = myclient["apilegislativo"] # == use apilegislativo
mycol = mydb["PRD"] # == db.iniciativasaprobadas...
iniciativas = response.json()
x = mycol.insert_many(iniciativas["iniciativas"])

#Importación a MongoDB Iniciativas por partido MC
url = "https://api.apilegislativo.com/iniciativa/partido/mc"

response = requests.request("GET", url, headers=headers, data=payload)

myclient = pymongo.MongoClient(client) # similar a ejecutar mongosh
mydb = myclient["apilegislativo"] # == use apilegislativo
mycol = mydb["Movimiento_ciudadano"] # == db.iniciativasaprobadas...
iniciativas = response.json()
x = mycol.insert_many(iniciativas["iniciativas"]) 

#Importación a MongoDB Iniciativas por partido PT
url = "https://api.apilegislativo.com/iniciativa/partido/pt"

response = requests.request("GET", url, headers=headers, data=payload)

myclient = pymongo.MongoClient(client) # similar a ejecutar mongosh
mydb = myclient["apilegislativo"] # == use apilegislativo
mycol = mydb["Partido_del_trabajo"] # == db.iniciativasaprobadas...
iniciativas = response.json()
x = mycol.insert_many(iniciativas["iniciativas"]) 

#Importación a MongoDB Iniciativas por partido PVEM
url = "https://api.apilegislativo.com/iniciativa/partido/pvem"

response = requests.request("GET", url, headers=headers, data=payload)

myclient = pymongo.MongoClient(client) # similar a ejecutar mongosh
mydb = myclient["apilegislativo"] # == use apilegislativo
mycol = mydb["PVEM"] # == db.iniciativasaprobadas...
iniciativas = response.json()
x = mycol.insert_many(iniciativas["iniciativas"]) 

#Importación a MongoDB Iniciativas por partido PES
url = "https://api.apilegislativo.com/iniciativa/partido/pes"

response = requests.request("GET", url, headers=headers, data=payload)

myclient = pymongo.MongoClient(client) # similar a ejecutar mongosh
mydb = myclient["apilegislativo"] # == use apilegislativo
mycol = mydb["PES"] # == db.iniciativasaprobadas...
iniciativas = response.json()
x = mycol.insert_many(iniciativas["iniciativas"]) 

#Importación a MongoDB Iniciativas por partido SP
url = "https://api.apilegislativo.com/iniciativa/partido/sp"

response = requests.request("GET", url, headers=headers, data=payload)

myclient = pymongo.MongoClient(client) # similar a ejecutar mongosh
mydb = myclient["apilegislativo"] # == use apilegislativo
mycol = mydb["SP"] # == db.iniciativasaprobadas...
iniciativas = response.json()
x = mycol.insert_many(iniciativas["iniciativas"]) 

#Importación a MongoDB Proposición por partido MORENA
url = "https://api.apilegislativo.com/proposicion/partido/morena"

response = requests.request("GET", url, headers=headers, data=payload)

myclient = pymongo.MongoClient(client) # similar a ejecutar mongosh
mydb = myclient["apilegislativo"] # == use apilegislativo
mycol = mydb["prop_MORENA"] # == db.iniciativasaprobadas...
iniciativas = response.json()
x = mycol.insert_many(iniciativas["proposiciones"]) 

#Importación a MongoDB Proposición por partido PRI
url = "https://api.apilegislativo.com/proposicion/partido/pri"

response = requests.request("GET", url, headers=headers, data=payload)

myclient = pymongo.MongoClient(client) # similar a ejecutar mongosh
mydb = myclient["apilegislativo"] # == use apilegislativo
mycol = mydb["prop_PRI"] # == db.iniciativasaprobadas...
iniciativas = response.json()
x = mycol.insert_many(iniciativas["proposiciones"]) 
