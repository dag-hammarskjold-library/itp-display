### imports

from flask import Flask,jsonify,render_template
from pymongo import MongoClient
from config import DATABASE_CONSTRING


app = Flask(__name__)
test="just a test"

# Route Definition

@app.route("/")
@app.route("/index")
def index():
    myMongoURI=DATABASE_CONSTRING
    myClient = MongoClient(myMongoURI)
    myDatabase=myClient.undlFiles
    myCollection=myDatabase['itp_sample_output']
    myRecords=myCollection.find()
    records=myRecords
    return render_template("index.html",records=records)

# Main program

if __name__ == '__main__':
  
    app.debug=True
    app.run()