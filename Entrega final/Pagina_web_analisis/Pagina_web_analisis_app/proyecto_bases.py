#!/usr/bin/env python3#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 27 16:02:08 2021

@author: bruno
"""
import requests
import pandas as pd
pd.set_option('display.max_colwidth', 1500)
pd.set_option("max_rows", None)
import pymongo
from pymongo import MongoClient
from datetime import datetime as dt
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
import os, yaml
from azure.storage.blob import ContainerClient
from django.conf import settings

def read_yaml_file(yaml_file):
    """ load yaml cofigurations """

    config = None
    try:
        with open(yaml_file, 'r') as f:
            config = yaml.safe_load(f)
    except:
        raise FileNotFoundError('Couldnt load the file')

    return config

def get_files(dir):
    with os.scandir(dir) as entries:
        for entry in entries:
            if entry.is_file() and not entry.name.startswith('.'):
                yield entry

def upload(files, connection_string, container_name):
    container_client = ContainerClient.from_connection_string(connection_string, container_name)
    print("Uploading files to blob storage... ")

    for file in files:
        blob_client = container_client.get_blob_client(file.name)
        with open(file.path,'rb') as data:
            blob_client.upload_blob(data)
            print (f'{file.name} uploaded to blob storage')
            os.remove(file)
            print (f'{file.name} removed from')

def iniciativa_id(id_ini):

    with open(os.path.join(settings.PROJECT_ROOT, 'conf/local/credentials_mongodb.txt')) as f:
        var = f.read()
    client = var

    client_cred = client
    client = MongoClient()
    client = MongoClient(client_cred)
    client.drop_database("consul_propuesta")

    with open(os.path.join(settings.PROJECT_ROOT, 'conf/token_api.txt')) as f:
        var = f.read()
        authorization = var

    payload={}
    headers = {
        'Authorization': authorization
    }

    url = "https://api.apilegislativo.com/iniciativa/" + str(id_ini) + '/'
    response = requests.request("GET", url, headers=headers, data=payload)

    myclient = pymongo.MongoClient(client_cred)
    mydb = myclient["consul_propuesta"]
    mycol = mydb["consulta_iniciativa"]
    iniciativas = response.json()
    x = mycol.insert_one(iniciativas)

    consul_inici = mycol.find()
    for i in consul_inici:
        iniciativa = i
    abstract_ini = normalize(iniciativa['abstract'])
    return [abstract_ini]

def normalize(s):
    replacements = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
    )
    for a, b in replacements:
        s = s.replace(a, b).replace(a.upper(), b.upper())
    return s

def id_token(id_tok):
  id = id_tok

  f = open(os.path.join(settings.PROJECT_ROOT, 'conf/token_api.txt'),'w')
  f.write(id)
  f.close()

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

def execute():
    cred1,cred2 = creds()

    data_apro = cred1.find()
    lista_ini_apro = list(data_apro)

    data_des = cred2.find()
    lista_ini_des = list(data_des)

    df_ini_apro = pd.DataFrame(lista_ini_apro)
    df_ini_des = pd.DataFrame(lista_ini_des)

    df_iniciativas = pd.concat([df_ini_apro,df_ini_des],axis=0)
    df_iniciativas.drop(columns='_id',inplace=True)

    abstract = df_iniciativas['abstract']

    lista_abstract = []

    for i in abstract:
        var = normalize(i)
        lista_abstract.append(var)

    NLTK_stop_words_list=stopwords.words('spanish')
    NLTK_stop_words_spanish = []

    for i in NLTK_stop_words_list:
        var = normalize(i)
        NLTK_stop_words_spanish.append(var)

    return NLTK_stop_words_spanish,df_iniciativas,lista_abstract

def id_propuesta_ley(id_iniciativa):

    NLTK_stop_words_spanish,df_iniciativas,lista_abstract = execute()

    tf_idf = TfidfVectorizer(lowercase=True, analyzer="word", stop_words=NLTK_stop_words_spanish, use_idf=True)

    tfidf_m = tf_idf.fit(lista_abstract)
    dtm = tfidf_m.transform(lista_abstract)

    tfidf_m = tfidf_m.vocabulary_

    today = dt.now()
    q = iniciativa_id(id_iniciativa)
    top = 5

    cv = CountVectorizer(lowercase=True, stop_words=NLTK_stop_words_spanish)
    q_tokens = cv.fit(q)
    tokens = q_tokens.get_feature_names()

    columns = {}
    for element in tokens:
        columns[element] = tfidf_m[element]

    # filtramos solo los términos que existen en nuestra DTM
    dtm_q = dtm[:,list(columns.values())].todense()
    # convertimos a DF para que la manipulación sea más sencilla
    tdm_df = pd.DataFrame(dtm_q)
    # sumamos td-idf de todos los documentos en la TDM para los tokens en el query
    tdidf_by_doc = tdm_df.apply(lambda x: x.sum(), axis=1)
    # top n de relevancia, por default 5
    top_n_relevance = tdidf_by_doc.sort_values(ascending=False).head(top)

    array_aux = top_n_relevance.index.values
    to_df = []

    for i in array_aux:
        to_df += [df_iniciativas.iloc[i,[0,5]]]

    df_ini_con = pd.DataFrame(to_df,index=array_aux)

    str_aux = "data/consulta_tfidf_"+ str(id_iniciativa) + "_" + str(today) + ".txt"



    data = open(os.path.join(settings.PROJECT_ROOT, str_aux),"w")
    L = [str(df_ini_con)]
    data.writelines(L)
    data.write('\n')
    S = [str(top_n_relevance)]
    data.writelines(S)
    data.close()

    config = read_yaml_file(os.path.join(settings.PROJECT_ROOT, 'conf/local/config.yaml'))
    data = get_files(os.path.join(settings.PROJECT_ROOT, 'data'))
    upload(data,config["azure_storage_connectionstring"],config["propuestas_container_name"] )

    stri = str(df_ini_con)
    stri_2 = str(top_n_relevance)
    lista = stri.split('\n')
    lista_2 = stri_2.split('\n')

    lista = lista[1:]
    lista_2 = lista_2[:-1]

    return {'abstract':lista,'relevancia':lista_2,'tokens':tokens}