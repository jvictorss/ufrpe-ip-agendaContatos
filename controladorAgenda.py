agenda = []


def cadastrarContato():
    print("#### CADASTRO DE CONTATO ####")
    while True:
        nome = input("Digite o nome do contato: ")
        sobrenome = input("Digite o sobrenome do contato: ")
        telefone = input("Digite o telefone do contato: ")
        if verificaContato(telefone):
            print("Este contato já existe.")
            break
        endereco = input("Digite o endereço do contato: ")
        numeroCasa = input("Digite o número da casa do contato: ")
        bairro = input("Digite o bairro do contato: ")
        cidadeEstado = input("Digite a cidade do contato seguida do estado. Ex.: Serra Talhada-PE: ")

        contato = [nome, sobrenome, telefone, endereco, numeroCasa, bairro, cidadeEstado]
        agenda.append(contato)
        option = int(input("Deseja cadastrar outro contato? [1] - Sim | [2] - Não (apenas número): "))
        if option != 1:
            break


def verificaContato(telefone):
    contatoExiste = False
    for i in range(0, len(agenda)):
        if telefone == agenda[i][2]:
            contatoExiste = True

    return contatoExiste


def listarContatos():
    print("#### LISTAR CONTATOS CADASTRADOS NA AGENDA ####")
    print("\n-----------------------------------------")
    for i in range(0, len(agenda)):
        print("Nome         : ", agenda[i][0], agenda[i][1])
        print("Telefone     : ", agenda[i][2])
        print("Endereço     : ", agenda[i][3])
        print("Número Casa  : ", agenda[i][4])
        print("Bairro       : ", agenda[i][5])
        print("Cidade-Estado: ", agenda[i][6])
        print("\n-----------------------------------------\n")


def editarContato():
    print("#### EDITAR CONTATO DA AGENDA ####")
    print("\n-----------------------------------------")
    qual = input("Insira o nome do contato que quer editar: ")

    try:
        for i in range(0, len(agenda)):
            if agenda[i][0] == qual:
                print("Nome         : ", agenda[i][0], agenda[i][1])
                print("Telefone     : ", agenda[i][2])
                print("Endereço     : ", agenda[i][3])
                print("Número Casa  : ", agenda[i][4])
                print("Bairro       : ", agenda[i][5])
                print("Cidade-Estado: ", agenda[i][6])
                print("\n-----------------------------------------\n")
                print("### OPÇÕES PARA EDIÇÃO ###")
                print("[1] - Nome")
                print("[2] - Sobrenome")
                print("[3] - Telefone")
                print("[4] - Endereço")
                print("[5] - Número Casa")
                print("[6] - Bairro")
                print("[7] - Cidade Estado")
                option = int(input("Digite o número do campo que quer editar: "))
                if option == 1:
                    novoCampo = input("Digite o novo Nome do contato: ")
                    agenda[i][0] = novoCampo
                    print("### CONTATO EDITADO COM SUCESSO ###")
                    print("CONFIRA ABAIXO COMO FICOU: ")
                    print("Nome         : ", agenda[i][0], agenda[i][1])
                    print("Telefone     : ", agenda[i][2])
                    print("Endereço     : ", agenda[i][3])
                    print("Número Casa  : ", agenda[i][4])
                    print("Bairro       : ", agenda[i][5])
                    print("Cidade-Estado: ", agenda[i][6])
                    print("\n-----------------------------------------")
                    input("Digite qualquer tecla para continuar")
                    break
                elif option == 2:
                    novoCampo = input("Digite o novo Sobrenome do contato: ")
                    agenda[i][1] = novoCampo
                    print("### CONTATO EDITADO COM SUCESSO ###")
                    print("CONFIRA ABAIXO COMO FICOU: ")
                    print("Nome         : ", agenda[i][0], agenda[i][1])
                    print("Telefone     : ", agenda[i][2])
                    print("Endereço     : ", agenda[i][3])
                    print("Número Casa  : ", agenda[i][4])
                    print("Bairro       : ", agenda[i][5])
                    print("Cidade-Estado: ", agenda[i][6])
                    print("\n-----------------------------------------")
                    input("Digite qualquer tecla para continuar")
                    break
                elif option == 3:
                    novoCampo = input("Digite o novo Telefone do contato: ")
                    agenda[i][2] = novoCampo
                    print("### CONTATO EDITADO COM SUCESSO ###")
                    print("CONFIRA ABAIXO COMO FICOU: ")
                    print("Nome         : ", agenda[i][0], agenda[i][1])
                    print("Telefone     : ", agenda[i][2])
                    print("Endereço     : ", agenda[i][3])
                    print("Número Casa  : ", agenda[i][4])
                    print("Bairro       : ", agenda[i][5])
                    print("Cidade-Estado: ", agenda[i][6])
                    print("\n-----------------------------------------")
                    input("Digite qualquer tecla para continuar")
                    break
                elif option == 4:
                    novoCampo = input("Digite o novo Endereço do contato: ")
                    agenda[i][3] = novoCampo
                    print("### CONTATO EDITADO COM SUCESSO ###")
                    print("CONFIRA ABAIXO COMO FICOU: ")
                    print("Nome         : ", agenda[i][0], agenda[i][1])
                    print("Telefone     : ", agenda[i][2])
                    print("Endereço     : ", agenda[i][3])
                    print("Número Casa  : ", agenda[i][4])
                    print("Bairro       : ", agenda[i][5])
                    print("Cidade-Estado: ", agenda[i][6])
                    print("\n-----------------------------------------")
                    input("Digite qualquer tecla para continuar")
                    break
                elif option == 5:
                    novoCampo = input("Digite o novo Número da Casa do contato: ")
                    agenda[i][4] = novoCampo
                    print("### CONTATO EDITADO COM SUCESSO ###")
                    print("CONFIRA ABAIXO COMO FICOU: ")
                    print("Nome         : ", agenda[i][0], agenda[i][1])
                    print("Telefone     : ", agenda[i][2])
                    print("Endereço     : ", agenda[i][3])
                    print("Número Casa  : ", agenda[i][4])
                    print("Bairro       : ", agenda[i][5])
                    print("Cidade-Estado: ", agenda[i][6])
                    print("\n-----------------------------------------")
                    input("Digite qualquer tecla para continuar")
                    break
                elif option == 6:
                    novoCampo = input("Digite o novo Bairro do contato: ")
                    agenda[i][5] = novoCampo
                    print("### CONTATO EDITADO COM SUCESSO ###")
                    print("CONFIRA ABAIXO COMO FICOU: ")
                    print("Nome         : ", agenda[i][0], agenda[i][1])
                    print("Telefone     : ", agenda[i][2])
                    print("Endereço     : ", agenda[i][3])
                    print("Número Casa  : ", agenda[i][4])
                    print("Bairro       : ", agenda[i][5])
                    print("Cidade-Estado: ", agenda[i][6])
                    print("\n-----------------------------------------")
                    input("Digite qualquer tecla para continuar")
                    break
                elif option == 7:
                    novoCampo = input("Digite a nova Cidade-Estado do contato: ")
                    agenda[i][6] = novoCampo
                    print("### CONTATO EDITADO COM SUCESSO ###")
                    print("CONFIRA ABAIXO COMO FICOU: ")
                    print("Nome         : ", agenda[i][0], agenda[i][1])
                    print("Telefone     : ", agenda[i][2])
                    print("Endereço     : ", agenda[i][3])
                    print("Número Casa  : ", agenda[i][4])
                    print("Bairro       : ", agenda[i][5])
                    print("Cidade-Estado: ", agenda[i][6])
                    print("\n-----------------------------------------")
                    input("Digite qualquer tecla para continuar")
                    break
    finally:
        input("Digite qualquer tecla para continuar.")


def excluirContato():
    print("#### EXCLUIR CONTATO DA AGENDA ####")
    qual = input("Insira o nome do contato que quer excluir: ")

    try:
        for i, contato in enumerate(agenda):
            if contato[0] == qual:
                print("Nome         : ", agenda[i][0], agenda[i][1])
                print("Telefone     : ", agenda[i][2])
                print("Endereço     : ", agenda[i][3])
                print("Número Casa  : ", agenda[i][4])
                print("Bairro       : ", agenda[i][5])
                print("Cidade-Estado: ", agenda[i][6])
                print("\n-----------------------------------------\n")
                option = int(
                    input("Cuidado! Deseja realmente excluir o contato? [1] - Sim | [2] - Não (apenas número)"))
                if option == 1:
                    agenda.pop(i)
                    print("Contato excluído com sucesso")
                    input("Digite qualquer tecla para continuar")
                    return
                else:
                    print("Ok. O contato não foi excluído.")
                    input("Digite qualquer tecla para continuar")
        print("Este contato não existe.")
        input("Digite qualquer tecla para continuar")

    finally:
        print("Este contato não existe.")


def buscarContato():
    print("#### BUSCAR CONTATO DA AGENDA ####")
    qual = int(input("Quer buscar o contato pelo Nome (digite 1) ou telefone (digite 2)? "))
    if qual == 1:
        nomeContato = input("Digite o nome do contato para buscar: ")
        try:
            for i, contato in enumerate(agenda):
                if contato[0] == nomeContato:
                    print("Nome         : ", agenda[i][0], agenda[i][1])
                    print("Telefone     : ", agenda[i][2])
                    print("Endereço     : ", agenda[i][3])
                    print("Número Casa  : ", agenda[i][4])
                    print("Bairro       : ", agenda[i][5])
                    print("Cidade-Estado: ", agenda[i][6])
                    print("\n-----------------------------------------\n")
        except:
            print("Não consegui encontrar este contato pelo nome.")
    elif qual == 2:
        numeroContato = input("Digite o número do telefone do contato para buscar: ")
        try:
            for i, contato in enumerate(agenda):
                if contato[2] == numeroContato:
                    print("Nome         : ", agenda[i][0], agenda[i][1])
                    print("Telefone     : ", agenda[i][2])
                    print("Endereço     : ", agenda[i][3])
                    print("Número Casa  : ", agenda[i][4])
                    print("Bairro       : ", agenda[i][5])
                    print("Cidade-Estado: ", agenda[i][6])
                    print("\n-----------------------------------------\n")
        finally:
            print("Não consegui encontrar este contato.")
