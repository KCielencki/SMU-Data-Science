import datetime as dt
import numpy as np
import pandas as pd
import json

from sqlHelper import SQLHelper
from flask import Flask, jsonify

app = Flask(__name__)

sqlHelper = SQLHelper()

@app.route("/api/v1.0/precipitation")
def precip():
    data = sqlHelper.getPrecipitation()
    return(jsonify(json.loads(data.to_json(orient='records'))))

@app.route("/api/v1.0/station")
def stations():
    data = sqlHelper.getStation()
    return(jsonify(json.loads(data.to_json(orient='records'))))

@app.route("/api/v1.0/tobs")
def active():
    data = sqlHelper.getActive()
    return(jsonify(json.loads(data.to_json(orient='records'))))

@app.route("/api/v1.0/startend")
def vacation():
    data = sqlHelper.getVacation()
    return(jsonify(json.loads(data.to_json(orient='records'))))

@app.route("/")
def home():
    return(
        f"Welcome to the Hawaii API"

        f"""
        <ul>
            <li> <a target = "_blank" href = '/api/v1.0/precipitation'> Get Total Precipitation</a></li>
            <li> <a target = "_blank" href = '/api/v1.0/station'> Get Total Precipitation</a></li>
            <li> <a target = "_blank" href = '/api/v1.0/tobs'> Get Total Precipitation</a></li>
            <li> <a target = "_blank" href = '/api/v1.0/precipitation'> Get Total Precipitation</a></li>
    )

if __name__ == "__main__":
    app.run(debug=True)