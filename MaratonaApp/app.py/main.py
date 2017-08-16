from Model.Pessoa import pessoa
from Model.Cliente import cliente
from Funcionario import funcionario
from Maratona import maratona

def main ():

    Funcionario = funcionario("maria")
    Cliente = cliente("jose")
    Maratona = maratona()
    maratona.correr(cliente)
    maratona.correr(funcionario)















    if __name__ == '__main__':
      main()
