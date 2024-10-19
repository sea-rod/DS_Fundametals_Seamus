import json
import pymongo

def load_file(path):
    with open(path) as file:
        data = json.load(file)
    return data

def calculate_total(data,city,price):
    return data['visa_rates'][city_country_mapping[city]] + price

city_country_mapping = {
    "new_york": "usa",
    "dallas": "usa",
    "beijing": "china",
    "colombo": "sri_lanka",
    "hong_kong": "china",
    "kandy": "sri_lanka",
    "wuhan": "china",
    "chicago": "usa"
}


if __name__ == "__main__":

    data = load_file("data.json")
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    

    print(data['visa_rates'][city_country_mapping["beijing"]])
    mydb = myclient["ticket_db"]



    for obj in mydb['ticket'].find({}):
        total = calculate_total(data,obj['visa_stampeed'][-1],int(obj['ticket_price']))
        print(f"id:{obj['ticket_id']} name:{obj['passenger_name']} total:{total}")
    