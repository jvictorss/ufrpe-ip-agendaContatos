from menuAgenda import menu
from controladorAgenda import *

def main():
    while True:
        opcaoMenu = menu()
        if opcaoMenu == 1:
            cadastrarContato()
        elif opcaoMenu == 2:
            listarContatos()
        elif opcaoMenu == 3:
            editarContato()
        elif opcaoMenu == 4:
            excluirContato()
        elif opcaoMenu == 5:
            buscarContato()
        elif opcaoMenu == 6:
            #Sair da aplicação
            print("Aplicação encerrada!")
            break
        else:
            print("Opção inválida.")
            input()
main()