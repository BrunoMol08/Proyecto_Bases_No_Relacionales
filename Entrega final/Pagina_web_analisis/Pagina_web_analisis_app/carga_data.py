#!/usr/bin/env python3#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 27 16:02:08 2021

@author: bruno
"""
import os
import pymongo
from pymongo import MongoClient
from django.conf import settings
import datetime as dt
import requests

def creds():
    
    with open(os.path.join(settings.PROJECT_ROOT, 'conf/local/credentials_mongodb.txt')) as f:
        var = f.read()
    client = var

    client_cred = client

    client = MongoClient()

    client = MongoClient(client_cred)

    mydatabase = client['apilegislativo']

    mycollection=mydatabase['iniciativasaprobadas']

    client_2=MongoClient()

    client_2 = MongoClient(client_cred)

    mydatabase_2 = client_2['apilegislativo']

    mycollection_2=mydatabase_2['iniciativasdesechadas']

    return mycollection,mycollection_2

def iniciativa_id(id,id_2,id_3,id_4,id_5):

    with open(os.path.join(settings.PROJECT_ROOT, 'conf/local/credentials_mongodb.txt')) as f:
        var = f.read()
    client = var

    client_cred = client
    client = MongoClient()
    client = MongoClient(client_cred)
    client.drop_database("consul_por_id")

    with open(os.path.join(settings.PROJECT_ROOT, 'conf/token_api.txt')) as f:
        var = f.read()
        authorization = var

    payload={}
    headers = {
        'Authorization': authorization
    }

    lista = [id,id_2,id_3,id_4,id_5]

    for i in lista:

        url = "https://api.apilegislativo.com/iniciativa/" + str(i) + '/'
        response = requests.request("GET", url, headers=headers, data=payload)

        myclient = pymongo.MongoClient(client_cred)
        mydb = myclient["consul_por_id"]
        mycol = mydb["consulta_iniciativa"]
        iniciativas = response.json()
        x = mycol.insert_one(iniciativas)

    return

def obtener_datos(tipo,ley,sexenio,cant):

    cant = int(cant)

    mycollection,mycollection_2 = creds()
    
    if tipo == 'aprobadas':
        
        if sexenio == 'epn':
            if ley == 'vacio':
                ley = ""
                agg_result_iniciativas= mycollection.aggregate([
                {"$addFields": {"status_date": { "$toDate": "$status_date"}}},
                {"$match":{"$and": [{"status_date" :{ "$gte": dt.datetime(2012,12,1,0,0,0,0)}},{"status_date": {"$lte": dt.datetime(2018,11,30,0,0,0,0)}},{"laws_mod":ley}]}},
                {"$limit":cant}
                ])
            else:
                agg_result_iniciativas= mycollection.aggregate([
                    {"$addFields": {"status_date": { "$toDate": "$status_date"}}},
                    {"$match":{"$and": [{"status_date" :{ "$gte": dt.datetime(2012,12,1,0,0,0,0)}},{"status_date": {"$lte": dt.datetime(2018,11,30,0,0,0,0)}},{"laws_mod":ley}]}},
                    {"$limit":cant}
                ])
        elif sexenio == 'amlo':
            if ley == 'vacio':
                ley = ""
                agg_result_iniciativas= mycollection.aggregate([
                {"$addFields": {"status_date": { "$toDate": "$status_date"}}},
                {"$match":{"$and": [{"status_date" :{ "$gte": dt.datetime(2018,12,1,0,0,0,0)}},{"status_date": {"$lte": dt.datetime(2024,11,30,0,0,0,0)}},{"laws_mod":ley}]}},
                {"$limit":cant}
                ])
            else:
                agg_result_iniciativas= mycollection.aggregate([
                    {"$addFields": {"status_date": { "$toDate": "$status_date"}}},
                    {"$match":{"$and": [{"status_date" :{ "$gte": dt.datetime(2018,12,1,0,0,0,0)}},{"status_date": {"$lte": dt.datetime(2024,11,30,0,0,0,0)}},{"laws_mod":ley}]}},
                    {"$limit":cant}
                ])
        else:
            if ley == 'vacio':
                ley = ""
                agg_result_iniciativas= mycollection.aggregate([
                {"$match":{"laws_mod":ley}},
                {"$limit":cant}
                ])
            else:
                agg_result_iniciativas= mycollection.aggregate([
                    {"$match":{"laws_mod":ley}},
                    {"$limit":cant}
                ])

    else:

        if sexenio == 'epn':
            if ley == 'vacio':
                ley = ""
                agg_result_iniciativas= mycollection_2.aggregate([
                {"$addFields": {"status_date": { "$toDate": "$status_date"}}},
                {"$match":{"$and": [{"status_date" :{ "$gte": dt.datetime(2012,12,1,0,0,0,0)}},{"status_date": {"$lte": dt.datetime(2018,11,30,0,0,0,0)}},{"laws_mod":ley}]}},
                {"$limit":cant}
                ])
            else:
                agg_result_iniciativas= mycollection_2.aggregate([
                    {"$addFields": {"status_date": { "$toDate": "$status_date"}}},
                    {"$match":{"$and": [{"status_date" :{ "$gte": dt.datetime(2012,12,1,0,0,0,0)}},{"status_date": {"$lte": dt.datetime(2018,11,30,0,0,0,0)}},{"laws_mod":ley}]}},
                    {"$limit":cant}
                ])
        elif sexenio == 'amlo':
            if ley == 'vacio':
                ley = ""
                agg_result_iniciativas= mycollection_2.aggregate([
                {"$addFields": {"status_date": { "$toDate": "$status_date"}}},
                {"$match":{"$and": [{"status_date" :{ "$gte": dt.datetime(2018,12,1,0,0,0,0)}},{"status_date": {"$lte": dt.datetime(2024,11,30,0,0,0,0)}},{"laws_mod":ley}]}},
                {"$limit":cant}
                ])
            else:
                agg_result_iniciativas= mycollection_2.aggregate([
                {"$addFields": {"status_date": { "$toDate": "$status_date"}}},
                {"$match":{"$and": [{"status_date" :{ "$gte": dt.datetime(2018,12,1,0,0,0,0)}},{"status_date": {"$lte": dt.datetime(2024,11,30,0,0,0,0)}},{"laws_mod":ley}]}},
                {"$limit":cant}
                ])
        else:
            if ley == 'vacio':
                ley = ""
                agg_result_iniciativas= mycollection_2.aggregate([
                {"$match":{"laws_mod":ley}},
                {"$limit":cant}
                ])
            else:
                agg_result_iniciativas= mycollection_2.aggregate([
                    {"$match":{"laws_mod":ley}},
                    {"$limit":cant}
                ])

    lista = []
    for i in agg_result_iniciativas:
        lista.append(i)
    return lista

def obtener_id(id,id_2,id_3,id_4,id_5):

    iniciativa_id(id,id_2,id_3,id_4,id_5)

    with open(os.path.join(settings.PROJECT_ROOT, 'conf/local/credentials_mongodb.txt')) as f:
        var = f.read()
    client = var

    client_cred = client
    client = MongoClient()
    client = MongoClient(client_cred)

    myclient = pymongo.MongoClient(client_cred)
    mydb = myclient["consul_por_id"]
    mycol = mydb["consulta_iniciativa"]

    iniciativas = []
    consul_inici = mycol.find()
    for i in consul_inici:
        iniciativas.append(i)
    return iniciativas