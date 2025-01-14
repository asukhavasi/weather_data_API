import flask
import pandas as pd


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
    filename = f"data/TG_STAID{str(station).zfill(6)}.txt"
    df= pd.read_csv(filename,skiprows=20,parse_dates=["    DATE"])
    temp = df.loc[df['    DATE']==date]['   TG'].squeeze()/10
    # temperature = 23
    return {"station":station,
            "date":date,
            "temperature":temp}

if __name__ == "__main__":
    app.run(debug=True)