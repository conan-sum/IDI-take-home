from flask import Flask, jsonify, request
from tweet import Tweets
from database import cols
import json


app = Flask(__name__)
data = Tweets("data", sep="\t")


# Initial landing point when pinging the API
@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "GET":
        return jsonify({"data": "API connection established"})


# Used for searching a keyword, and returns the results in JSON format
@app.route("/search/<string:term>", methods=["GET"])
def search(term):
    # Generate a summary of the search term, and store the result in MongoDB
    payload = data.search(term)
    cols.insert_one(json.loads(json.dumps(payload)))
    return jsonify({"results": payload})
