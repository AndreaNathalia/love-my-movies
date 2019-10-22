from flask import Flask, render_template
import requests
import json, sys

movies = Flask(__name__)

discover = requests.get("https://api.themoviedb.org/3/discover/movie?api_key=2b785ba178972f95b1650f77ecd8f8ae&language=en-US&sort_by=popularity.desc&include_adult=false&include_video=false&page=1")
data_discover = discover.json()


with open('discover_movies.json') as file:
    data = json.load(file)

# Variables con info json 
#(IMAGENES)
img1 = data['results'][0]['poster_path']


# (TITULOS)
title1 = data['results'][0]['title']
title2 = data['results'][1]['title']
title3 = data['results'][2]['title']
title4 = data['results'][3]['title']
title5 = data['results'][4]['title']
title6 = data['results'][5]['title']
title7 = data['results'][6]['title']
title8 = data['results'][7]['title']
title9 = data['results'][8]['title']

title10 = data['results'][9]['title']
title11 = data['results'][10]['title']
title12 = data['results'][11]['title']
title13 = data['results'][12]['title']
title14 = data['results'][13]['title']

# (OVERVIEWS)
overview1 = data['results'][0]['overview']
overview2 = data['results'][1]['overview']
overview3 = data['results'][2]['overview']
overview4 = data['results'][3]['overview']
overview5 = data['results'][4]['overview']
overview6 = data['results'][5]['overview']
overview7 = data['results'][6]['overview']
overview8 = data['results'][7]['overview']
overview9 = data['results'][8]['overview']

overview10 = data['results'][9]['overview']
overview11 = data['results'][10]['overview']
overview12 = data['results'][11]['overview']
overview13 = data['results'][12]['overview']
overview14 = data['results'][13]['overview']


@movies.route("/")
def ui():
    return render_template('ui.html', 
    data = data, title1 = title1, title2 = title2, title3 = title3, title4 = title4, title5 = title5, title6 = title6,
    title7 = title7, title8 = title8, title9 = title9, title10 = title10, title11 = title11, title12 = title12, title13 = title13, title14 = title14,
    overview1 = overview1, overview2 = overview2, overview3 = overview3, overview4 = overview4,
    overview5 = overview5, overview6 = overview6, overview7 = overview7, overview8 = overview8, overview9 = overview9, overview10 = overview10, overview11 = overview11, overview12 = overview12, overview13 = overview13, overview14 = overview14,
    img1 = img1)

if __name__ == '__main__':
    movies.run(host="0.0.0.0", debug=True)


