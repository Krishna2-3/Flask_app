from flask import Flask
import pymongo
from pymongo import MongoClient
import time
app = Flask(__name__)

# Replace placeholders with actual values
password = "Vivek6904"
username = "pyany"

# Construct MongoDB connection URI
uri = f"mongodb+srv://{username}:{password}@krishna.njty3hn.mongodb.net/?retryWrites=true&w=majority&appName=krishna"

# Connect to MongoDB
client = MongoClient(uri)
db = client['ADS']
collection = db['ADS']

@app.route("/")
def index():
    try:
        count = collection.count_documents({})
        if count > 0:  # Check if there are any documents returned
            result = collection.find()
            time.sleep(2)
            first_document = result[0] #problem arrise from this line.
            # Access the first document
            time.sleep(2)
            print(first_document)
        print("success123444222")
        return "success"
    except Exception as e:
        print("this is error:",e)
        return "failed"

if __name__ == '__main__':
    app.run()
