import flask
import pandas



app = flask.Flask(__name__)

@app.route("/")
def home():
    return flask.render_template("home.html")

@app.route("/about")
def about():
    return flask.render_template("about.html")

@app.route("/contact")
def contact():
    return flask.render_template("contact.html")

@app.route("/api/v1/<station>/<date>")
def api(station,date):
    # df=pandas.read_csv()
    temperature = 23
    return {"station":station,
            "date":date,
            "temperature":temperature}

if __name__ == "__main__":
    app.run(debug=True)