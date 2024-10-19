from operations import retrive_data,insert_data
import mysql.connector

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
