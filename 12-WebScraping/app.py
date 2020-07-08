from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scraper

app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

@app.route("/")
def index():
    mars = mongo.db.mars.find_one()
    return render_template("index.html", mars=mars)


@app.route("/scrape")
def scrape():
    mars_app = mongo.db.mars
    mars = scraper.marsScraper()
    mars_app.replace_one({},mars,upsert=True)
    return "Sucessful scrapping"
     
    # mars_app.update_many(
    #     {'active': 1},
    #     {"$set": {'active': 0}
    #     }
    # )

    # mars_app.insert_one(mars)
    
    # return redirect('/')


if __name__ == "__main__":
    app.run()