from pymongo import MongoClient

# Creating instance of mongo client
client = MongoClient("mongodb://intern_23:intern%40123@192.168.0.220:2717/interns_b2_23")
# Creating database
book_db = client.interns_b2_23

# # Creating document
book_1 = book_db.Sridevi
