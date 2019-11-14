### imports

from flask import Flask,jsonify,render_template
from pymongo import MongoClient
from config import DATABASE_CONSTRING,URL_PREFIX
from data import myData


app = Flask(__name__)
test="just a test 02"

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
    number=myCollection.find().count()
    sideA=round(number/2)+1
    sideB=number-sideA
    return render_template("index.html",records=records,number=number,sideA=sideA,sideB=sideB)


@app.route("/indextospeeches")
def indexToSpeeches():
    return render_template("indextospeeches.html",records=myData,myURL=URL_PREFIX)

# Main program

if __name__ == '__main__':
  
    app.debug=True
    app.run()