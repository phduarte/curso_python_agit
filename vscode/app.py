from flask import Flask
from flask_restful import Resource, Api
from resources.conta import ContasBancarias

app = Flask(__name__)
api = Api(app)
    
api.add_resource(ContasBancarias, '/contas')

if __name__ == '__main__':
    app.run(debug=True)
