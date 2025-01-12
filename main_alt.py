import flask


app_alt = flask.Flask(__name__)

@app_alt.route("/")
def home():
    return flask.render_template("home_alt.html")

@app_alt.route("/api/v1/<word>")
def api(word):
    cap_word = word.upper()
    return {"definition":cap_word,
            "word":word}



if __name__ == "__main__":
    app_alt.run(debug=True,port=5001)