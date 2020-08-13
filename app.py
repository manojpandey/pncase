# -*- coding: utf-8 -*-
# Author: @manojpandey

import os
from datetime import datetime
from flask import Flask, jsonify
from pymongo import MongoClient

# Setup
app = Flask(__name__)
client = MongoClient('localhost', 27017)
db = client.pubnative
collection = db.case_study

@app.route('/')
def root():
    return "Hello, Pubnative!"

@app.route('/promotions/<promotion_id>')
def api(promotion_id: str):
    """ API logic

    Returns JSON object of the data inside the database
    where id = promotion_id passed as parameter to the route. 
    """

    data = collection.find_one({"_id": promotion_id})
    if data is not None:
        data['id'] = data.pop('_id')
        return jsonify(formatter(data))
    else:
        return jsonify({"Error": "Not found"})

def formatter(data: dict) -> dict:
    """
    Formats some of the data objects.
    """
    datetime_object = datetime.strptime(data['expiration_date'], '%Y-%m-%d %H:%M:%S %z %Z')
    formatted_date = datetime_object.strftime('%Y-%m-%d %H:%M:%S')
    data['expiration_date'] = formatted_date
    data['price'] = f"{data['price']:.2f}"
    return data

# When developing locally, this will use port 8000, 
# in production (for ex. Heroku) will set the PORT environment variable.
if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 8000.
    port = int(os.environ.get('PORT', 8000))
    app.run(host='0.0.0.0', port=port, debug=False)