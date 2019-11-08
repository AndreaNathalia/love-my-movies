from flask import Flask, render_template
import requests
import json, sys

movies = Flask(__name__)

discover = requests.get("https://api.themoviedb.org/3/discover/movie?api_key=2b785ba178972f95b1650f77ecd8f8ae&language=en-US&sort_by=popularity.desc&include_adult=false&include_video=false&page=1")
data_discover = discover.json()


with open('discover_movies.json') as file:
    data = json.load(file)

# Listas para discover
titles = []
overviews = []
pic = []

for i in data['results']:
    titles.append(i['title'])
    overviews.append(i['overview'])
    pic.append(i['poster_path'])

with open('trending_movies.json') as file:
    data2 = json.load(file)

# Listas para trending
titles2 = []
overviews2 = []
pic2 = []

for x in data2['results']:
    titles2.append(x['title'])
    overviews2.append(x['overview'])
    pic2.append(x['poster_path'])



@movies.route("/")
def ui():
    return render_template('ui.html', 
    data = data, data2 = data2,
    titles = titles, overviews = overviews, pic = pic,
    titles2 = titles2, overviews2 = overviews2, pic2 = pic2)

if __name__ == '__main__':
    movies.run(host="0.0.0.0", debug=True)


