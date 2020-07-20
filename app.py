# Section 10.5.1

# Import dependencies
# use Flask to render a template
# use PyMongo to interact with Mongo database
# convert from Jupyter notebook to Python to use the scraping code
from flask import Flask, render_template
from flask_pymongo import PyMongo
import scraping

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
# tells Python that our app will connect to Mongo using a URI, 
# URI = uniform resource identifie, it is similar to a URL
# URI is saying that the app can reach Mongo through localhost server 
# using port 27017, using a database named ”mars_app”
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

# Setup the routes

# tell Flask what to display when we’re looking at the home page
@app.route("/")
def index():
   mars = mongo.db.mars.find_one()
   return render_template("index.html", mars=mars)

@app.route("/scrape")
def scrape():
   mars = mongo.db.mars
   mars_data = scraping.scrape_all()
   mars.update({}, mars_data, upsert=True)
   return "Scraping Successful!"

if __name__ == "__main__":
   app.run()