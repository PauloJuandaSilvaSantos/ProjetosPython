from Pessoa import Pessoa

class Funcionario(Pessoa):
    def __init__(self,nome):
        super (Funcionario,self).__init__(nome)


    def andar(self):
        print ("funcionario correndo de forma generica")

    def pagar(self):
        print("funcionario pagaando como pessoa")
