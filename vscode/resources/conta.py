from flask_restful import Resource

contas = [

{
    'numero_conta': '01',
    'nome': 'Alice',
    'Saldo': 10000,
},
{
    'numero_conta': '02',
    'nome': 'Bob',
    'Saldo': 12000,
},
{
    'numero_conta': '03',
    'nome': 'Carol',
    'Saldo': 15000,
}

]

class ContasBancarias(Resource):
    
    def get(self):
        return { 'contas' : contas }
    
    def post(self):
        pass
    
    def put(self):
        pass
    
    def delete(self):
        pass


class Conta(Resource):

    def get(self, numero_conta):
        for conta in contas:
            if conta['numero_conta'] == numero_conta:
                return conta
        return { 'mensagem' : 'conta nao achada' }, 404
    
    def post(self, numero_conta):
        pass
    
    def put(self, numero_conta):
        pass
    
    def delete(self, numero_conta):
        pass