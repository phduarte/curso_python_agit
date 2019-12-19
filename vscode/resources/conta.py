from flask_restful import Resource, reqparse

contas = [

{
    'numero_conta': '01',
    'nome': 'Alice',
    'Saldo': 10000
},
{
    'numero_conta': '02',
    'nome': 'Bob',
    'Saldo': 12000
},
{
    'numero_conta': '03',
    'nome': 'Carol',
    'Saldo': 15000
}

]

class ContasBancarias(Resource):
    
    def get(self):
        return { 'contas' : contas }
    

class Conta(Resource):

    argumentos = reqparse.RequestParser()
    argumentos.add_argument('nome', type=str)
    argumentos.add_argument('Saldo', type=float)

    # implementando achar_conta
    def achar_conta(numero_conta):
        for conta in contas:
            if conta['numero_conta'] == numero_conta:
                return conta
        return None        

    def get(self, numero_conta):
        conta = Conta.achar_conta(numero_conta)
        if conta == None:
            return { 'mensagem' : 'conta nao achada' }, 404
        else:
            return conta
    
    def post(self, numero_conta):
        conta = Conta.achar_conta(numero_conta)
        if conta != None:
            return 'conta existente', 404

        json = Conta.argumentos.parse_args()
        
        nova_conta = { 
            'numero_conta': numero_conta,
            'nome': json['nome'],
            'Saldo': json['Saldo']
        }

        contas.append(nova_conta)
        return nova_conta, 200

    def put(self, numero_conta):

        json = Conta.argumentos.parse_args()
        nova_conta = { 'numero_conta': numero_conta, **json }
        conta = Conta.achar_conta(numero_conta)

        if conta:
            conta.update(nova_conta)
            return nova_conta, 200
        else:
            contas.append(nova_conta)
            return nova_conta, 201

    
    def delete(self, numero_conta):
        global contas 
        contas = [ conta for conta in contas if conta['numero_conta'] != numero_conta ]
        return 'conta deletada'