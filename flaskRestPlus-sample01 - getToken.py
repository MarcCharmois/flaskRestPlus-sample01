from flask import Flask
from flask_restplus import Resource, Api

app = Flask(__name__)                  #  Create a Flask WSGI appliction
api = Api(app)                         #  Create a Flask-RESTPlus API

@api.route('/token')                   #  Create a URL route to this resource
class Token(Resource):            #  Create a RESTful resource
    def get(self):                     #  Create GET endpoint
        return {'token': 'gerg51-1s51fv-561dvsvd-fvkiy1d15d'}

if __name__ == '__main__':
    app.run(debug=True)                #  Start a development server