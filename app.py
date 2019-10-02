from flask import Flask, render_template
from pymongo import MongoClient

client = MongoClient()
db = client.Playlister
playlists = db.playlists

app = Flask(__name__)
# @app.route('/')
# def index():
#     # return 'Hello, World!'
#     return render_template('home.html', msg='Flask is cool!!')

# playlists = [
#     { 'title': 'XXXTENTACION', 'description': 'SAD!' },
#     { 'title': 'A$AP Rocky', 'description': 'Babushka boi' }
# ]

@app.route('/')
def playlists_index():
    return render_template('playlists_index.html', playlists=playlists.find())

if __name__  == '__main__':
    app.run(debug=True)