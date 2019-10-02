from flask import Flask, render_template, request, redirect, url_for
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

@app.route('/playlists/new')
def playlists_new():
    return render_template('playlists_new.html')

@app.route('/playlists', methods=['POST'])
def playlists_submit():
    playlist = {
        'title': request.form.get('title'),
        'description': request.form.get('description'),
        'videos': request.form.get('videos').split()
    }
    playlists.insert_one(playlist)
    # print(request.form.to_dict())
    return redirect(url_for('playlists_index'))



if __name__  == '__main__':
    app.run(debug=True)
