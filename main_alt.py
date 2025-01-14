import flask
import pandas

app_alt = flask.Flask(__name__)
df = pandas.read_csv("C:/Users/asukh/Documents/Weather_API/static"
                     "/dictionary"
                     ".csv")
@app_alt.route("/")
def home():
    return flask.render_template("home_alt.html")

@app_alt.route("/api/v1/<word>")
def api(word):
    definition = df.loc[df["word"]==word]["definition"].squeeze()
    result = {"word":word,"definition": definition}

    return result



if __name__ == "__main__":
    app_alt.run(debug=True,port=5001)