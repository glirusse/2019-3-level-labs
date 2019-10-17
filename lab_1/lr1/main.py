import json
from datetime import datetime

from flask import Flask, render_template, url_for
from werkzeug.utils import redirect

from config import Configuration

app = Flask(__name__)
app.config.from_object(Configuration)

now = datetime.now()
time = now.strftime("%d/%m/%Y %H:%M:%S")

@app.route('/')
def excellent():
    with open("articles.json", "r") as file:
        data = json.load(file)
        link = data["url"]
        articles = data["articles"]
    return render_template('page.html', link=link, list=articles, time = time)


@app.route('/redo/', methods=['GET'])
def refresh():
    return redirect(url_for("excellent"))

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000)
