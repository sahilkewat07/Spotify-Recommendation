from flask import Flask, render_template, request
from recommender import recommend_songs

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        song = request.form['song']
        results = recommend_songs(song)
        return render_template('result.html', song=song, results=results)
    return render_template('index.html')

if __name__ == '_main_':
    app.run(debug=True)