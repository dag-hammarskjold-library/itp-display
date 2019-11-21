### imports

from flask import Flask,jsonify,render_template,url_for
from pymongo import MongoClient
from config import DATABASE_CONSTRING,URL_PREFIX


app = Flask(__name__)
test="just a test 02"

myMongoURI=DATABASE_CONSTRING
myClient = MongoClient(myMongoURI)
myDatabase=myClient.undlFiles
myCollection=myDatabase['itp_sample_output']


# Route Definition
@app.route("/")
@app.route("/main")
def main():
    return render_template("main.html")

@app.route("/itpp_itpsor")
def itpp_itpsor():
    myRecords=myCollection.find()
    records=myRecords
    return render_template("itpsor.html",records=records,number=records.count())

@app.route("/itpp_itpitsp")
def itpp_itpitsp():
    myRecords=myCollection.find({'section': "itpitsp"},{'itshead':1, 'itssubhead':1, 'itsentry':1})
    records=myRecords
    return render_template("itpitsp.html",records=records,myURL=URL_PREFIX)

@app.route("/itpp_itpitsc")
def itpp_itpitsc():
    myRecords=myCollection.find({'section': "itpitsc"}, {'itshead':1, 'itssubhead':1, 'itsentry':1, 'docsymbol': 1})
    records=myRecords
    return render_template("itpitsc.html",records=records,myURL=URL_PREFIX)


@app.route("/itpp_itpitss")
def itpp_itpitss():
    myRecords=myCollection.find({'section': "itpitss"}, {'itshead':1, 'itssubhead':1, 'itsentry':1, 'docsymbol': 1})
    records=myRecords
    return render_template("itpitss.html",records=records,myURL=URL_PREFIX)

# Main program

if __name__ == '__main__':
  
    app.debug=True
    app.run()