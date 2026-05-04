from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

API_KEY = "eae290f2"
BASE_URL = "http://www.omdbapi.com/"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search")
def search():
    query = request.args.get("q", "")
    page = request.args.get("page", 1)
    if not query:
        return jsonify({"error": "No query provided"}), 400

    response = requests.get(BASE_URL, params={
        "apikey": API_KEY,
        "s": query,
        "page": page
    })
    return jsonify(response.json())

@app.route("/movie/<imdb_id>")
def movie_detail(imdb_id):
    response = requests.get(BASE_URL, params={
        "apikey": API_KEY,
        "i": imdb_id,
        "plot": "full"
    })
    return jsonify(response.json())

if __name__ == "__main__":
    app.run(debug=True)
