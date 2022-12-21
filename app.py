# Import dependencies <>
import pandas as pd
import sqlalchemy
from pprint import pprint
from flask import Flask, jsonify, render_template
#from flask_cors import CORS
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy import create_engine, func

# Create engine to wardata.sqlite
engine = create_engine("sqlite:///data/wardata.sqlite")
DBSession = sessionmaker(bind=engine)
session = DBSession()

Base = declarative_base()
class Baseball(Base):
    __tablename__ = "baseball"
    player_id = Column(Integer, primary_key=True)
    rank_in_country = Column(Integer)
    player_name = Column(String)
    war = Column(Float)
    year_min = Column(Integer)
    year_max = Column(Integer)
    age_range = Column(String)
    birth_location = Column(String)
    country = Column(String)
    position = Column(String)

variable = session.query(Baseball)

#Sample Query
new_df = pd.read_sql("SELECT * FROM baseball", engine)
#Baseball Dictionary
baseball_dict = new_df.to_dict("records")

geojson_list = []
for player in baseball_dict:
    for e in player:
        geojson_dict = {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [player["Latitude"], player["Longitude"]]
                },
                "properties": {
                    "player_id": player["player_id"],
                    "player_name": player["player_name"],
                    "age_range": player["age_range"],
                    "birth_location": player["birth_location"],
                    "country": player["country"],
                    "position": player["position"],
                    "rank_in_country": player["rank_in_country"],
                    "war": player["war"],
                    "year_max": player["year_max"],
                    "year_min": player["year_min"]
                }
        }
    geojson_list.append(geojson_dict)

    
geojson_dict_api = {}
geojson_dict_api["type"] = "FeatureCollection"
geojson_dict_api["metadata"] = {"title": "Baseball Player WAR DATA, MLB",
                                "status": 200,
                                "api": 1.0}
geojson_dict_api["features"] = geojson_list

# Flask Setup
app = Flask(__name__)

# Flask Routes
@app.route("/")
def homepage():
    return render_template("index.html")

@app.route("/api/v1.0/baseball")
def baseball():
    """Return baseball data as json"""
    return jsonify(baseball_dict)

@app.route("/api/v1.0/country/<country>")
def country(country):
    """Return players without missing data as json by country"""
    temp_df = pd.read_sql(f"SELECT * FROM baseball WHERE country LIKE '{country.upper()}';", engine)
    if temp_df.empty == False:
        return jsonify(temp_df.to_dict("records"))
    else:
        return jsonify({"error": "Country not found or doesn't contain records."})
    
@app.route("/api/v1.0/position/<position>")
def position(position):
    """Return players without missing data as json by position"""
    temp_df = pd.read_sql(f"SELECT * FROM baseball WHERE position LIKE '{position.capitalize()}';", engine)
    if temp_df.empty == False:
        return jsonify(temp_df.to_dict("records"))
    else:
        return jsonify({"error": "Country not found or doesn't contain records."})

@app.route("/api/v1.0/topten/<country>")
def top_ten_by_country(country):
    """Return top ten players without missing data ordered by war as json by country"""
    temp_df = pd.read_sql(f"SELECT * FROM baseball WHERE country LIKE '{country.upper()}' ORDER BY war LIMIT 10;", engine)
    if temp_df.empty == False:
        return jsonify(temp_df.to_dict("records"))
    else:
        return jsonify({"error": "Country not found or doesn't contain records."}) 
    
@app.route("/api/v1.0/geojson")
def geojson():
    """Return baseball data in geojson format"""
    return jsonify(geojson_dict_api)
    
if __name__ == "__main__":
    app.run(debug=True, use_reloader = False)