#!/usr/bin/python
import pymongo
import urllib3
import json

http = urllib3.PoolManager()
url = "https://api.coingecko.com/api/v3/exchange_rates"

print("-----------------------------------------------------------------------------------------------------------")
print(" The script Which collects data from Crpto currency values API and store data to DB: mydatabase and to collection: values")

print(" Prerequisites : pymongo,urllib3 and mongo DB running in localhost:27017 port")
print("-----------------------------------------------------------------------------------------------------------")

try:
    response = http.request('GET', url)
    data = json.loads(response.data)
    fp = open('coingecko.json','w')
    fp.write(str(data))
    fp.close()
    
except:
    print ("Error occured")

#Connect to the Mongo DB local instancei port 27017

myclient = pymongo.MongoClient("mongodb://localhost:27017/")


currencies_db = myclient["mydatabase"] # Created a database
mycol = currencies_db["values"] # Created a collection

print("Available databases in DB:")
print(myclient.list_database_names())
#List the available Databses

#Droping existing DB

mycol.drop()

#Inserting json data to the DB
x=mycol.insert_one(data)

#Display the insert_id generated after transaction
print("Data is inserted to DB _id: %s"%(x.inserted_id))



#Disply all the data from DB usw below

def find_all():
    for x in mycol.find():
        print(x)


#function to get specified values,here currencies btc
def find_values():
    myquery = { "rates.btc.name": "Bitcoin" }
    mydoc = mycol.find(myquery,{"rates.btc.name":1,"rates.btc.value":1,"rates.btc.unit":1,"rates.btc.type":1})
    for x1 in mydoc:
        print(x1)
    
#Display data from DB related to btc currencies

find_values()

def func_par_data(parm):
    """Defined Useful queries functions"""
    myquery = { }

    req_data =  {"rates.cur.name":1,"rates.cur.value":1,"rates.cur.unit":1,"rates.cur.type":1}
    print(type(req_data))
    for k,v in req_data.items():
        req_data
    req_data_desired = { k.replace('cur', parm): v for k, v in req_data.items() }
    mydoc = mycol.find(myquery, req_data_desired) 
    for items in mydoc:
        print(items)

func_par_data("bnb")
func_par_data("bdt")
func_par_data("eth")
func_par_data("inr")


print("-----------------------------------------------------------------------------------------------------------")

