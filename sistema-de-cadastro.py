contatos = []
dicionario = {}


while True:
    #Interface do sistema
    print("------Menu do Sistema------")
    opcao1 = print("1 - Adicionar Contatos")
    opcao2 = print("2 - Listar Contatos")
    opcao3 = print("3 - Buscar Contatos")
    opcao4 = print("4 - Sair")
    escolha = input("Digite a opção: ")
    #Lógica da escolha
    if escolha == "1":
        print("-- Adicione o contato --")
    
        nome = input("Digite o nome:")
        telefone = input("Digite o telefone:")
        email = input("Digite o email:")
         
        dicionario["nome"] = nome
        dicionario["telefone"] = telefone
        dicionario["email"] = email
    
        contatos.append(dicionario)

        print("\n Contato Adicionado! \n")

    elif escolha == "2":
       for dicionario in contatos:
           print("------Lista de contatos------")
           print(contatos)
           print("\n")
    
    elif escolha == "3":
        busca = int(input("Digite o ID do contato:"))
        detalhes = contatos[busca]

        print(f"Nome:{detalhes[nome]} ")
        print(f"Telefone:{detalhes[telefone]} ")
        print(f"Email:{detalhes[email]} ")
        

    elif escolha == "4":
        print("Fim do programa...")
        break
        
    else:
        print("Opção Inválida")    
        


    








    
