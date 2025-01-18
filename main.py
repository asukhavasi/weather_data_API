import flask
import pandas as pd


app = flask.Flask(__name__)

stations  = pd.read_csv("C:/Users/asukh/Documents/Weather_API/data/stations.txt"
                     "",skiprows=17)
stations_filtered = stations[['STAID','STANAME                                 ']]
@app.route("/")
def home():
    return flask.render_template("home.html",data = stations_filtered.to_html())

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

@app.route("/api/v1/<station>")
def all_data(station):
    filename = f"data/TG_STAID{str(station).zfill(6)}.txt"
    df = pd.read_csv(filename,skiprows=20,parse_dates=["    DATE"])
    df_filtered = df[["STAID",' SOUID',"    DATE","   TG"]]
    # return flask.render_template("home.html",data1=df_filtered.to_html())
    return df_filtered.to_dict(orient="records")

@app.route("/api/v1/yearly/<station>/<year_input>")
def station_yearly(station,year_input):
    filename = f"data/TG_STAID{str(station).zfill(6)}.txt"
    df = pd.read_csv(filename,skiprows=20)
    df['    DATE']=df['    DATE'].astype(str)
    result = df[df['    DATE'].str.startswith(str(year_input))]
    # return date_temp.to_dict(orient="records")
    # result = df[df['    DATE'].dt.year == int(year_input)]
    return result.to_dict(orient="records")





if __name__ == "__main__":
    app.run(debug=True)