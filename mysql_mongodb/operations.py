import mysql.connector
from pymongo import MongoClient


def retrive_data(conn, query) -> tuple:
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    cursor.close()
    return results


def insert_data(cat, prod):
    client = MongoClient(
        "mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+2.2.15"
    )
    db = client["ecom"]
    m_cat = db["category"]

    # Dictionary to map category IDs to their names
    cat_dict = {}
    for id, name in cat:
        cat_dict[id] = {"name": name, "products": []}

    # Populate the products into the categories
    for _, name, price, cat_id in prod:
        if cat_id in cat_dict:
            product = {
                "name": name,
                "price": float(price)
            }
            cat_dict[cat_id]["products"].append(product)
    
    # Insert or update categories with products
    for cat_id, cat_data in cat_dict.items():
        # Update existing category or insert new category
        m_cat.update_one(
            {"_id": cat_id},
            {"$set": cat_data},
            upsert=True
        )




if __name__ == "__main__":
    conn = mysql.connector.connect(
        host="localhost", user="root", password="root", database="ecom"
    )

    print("######################## PRODUCTS ##################")
    prod = retrive_data(conn, "Select * from product")
    for row in prod:
        print(row)

    print("######################## CATEGORY ##################")
    cat = retrive_data(conn, "Select * from category")
    for row in cat:
        print(row)

    insert_data(cat,prod)
    conn.close()
