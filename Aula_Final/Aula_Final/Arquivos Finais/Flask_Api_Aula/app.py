from flask import Flask
from flask_restful import Api
from resources.conta import ContasBancarias, Conta

app = Flask(__name__)
api = Api(app)
    
api.add_resource(ContasBancarias, '/contas')
# adicionando novo endpoint
api.add_resource(Conta, '/contas/<string:numero_conta>')

if __name__ == '__main__':
    app.run(debug=True)
