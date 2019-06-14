import flask                            #import flask library     
import datetime
from flask import jsonify, request

app = flask.Flask(__name__)
app.config["DEBUG"] = True

books = [
    {'no': 1, 
     'title' : 'Book one', 
     'author' : 'Name 0ne',
     'year': '1991'}, 

    {'no': 2, 
     'title' : 'Book two', 
     'author' : 'Name two',
     'year': '1992'}, 

    {'no': 3, 
     'title' : 'Book three', 
     'author' : 'Name three',
     'year': '1993'},

    {'no': 4, 
     'title' : 'Book four', 
     'author' : 'Name four',
     'year': '1994'}, 

    {'no': 5, 
     'title' : 'Book five', 
     'author' : 'Name five',
     'year': '1995'}
]

@app.route('/books', methods=['GET'])
def api_no():

    if 'no' in request.args:
        no = int(request.args['no'])
    else:
        return "Error: No not provided"

    results = []

    for book in books:
        if book['no'] == no:
            results.append(book)

    return jsonify(results)

@app.route('/', methods=['GET'])
def home():
    return "<html><h1>Heading</h1><p><h2>Sub heading</h2></html>"

@app.route('/timeofserver', methods=['GET'])
def api_timeofserver():
    return str(datetime.datetime.now())

@app.errorhandler(404)
def page_not_found(e):
    return "<html><H1>Not today babes<H1></html>"

@app.route('/books/all', methods=['GET'])
def api_all():
    return jsonify(books)



app.run()
