#SISTEMA DE GERENCIAMENTO DE CONTATOS
# EQUIPE: João Pedro Alves/ Laura / Mateus / Victor 
 

#Criando a lista    
contatos = []

#Criando o Loop
while True:
    #Interface do sistema
    print("\n ------ Sistema de Gerenciamento de Contatos ------")
    print("1 - Adicionar Contatos")
    print("2 - Listar Contatos")
    print("3 - Buscar Contatos")
    print("0 - Sair")
    escolha = input("Digite a opção: ")
    #Adicionando contatos
    if escolha == "1":
        print("-- Adicione o contato --")
    
        nome = input("Digite o nome:")
        telefone = input("Digite o telefone:")
        email = input("Digite o email:")
        #Criação do dicionário para armazenamento do contato
        dicionario = {}
        dicionario["nome"] = nome
        dicionario["telefone"] = telefone
        dicionario["email"] = email
        
        contatos.append(dicionario)
        print("Salvo!")

    #Puxando os itens da lista para mostrar ao usuário os contatos
    elif escolha == "2":
        print("\n --- Lista de Contatos ---")
        for item in contatos:
            print(item)

    #Puxando os itens da lista de acordo com o nome que foi adicionado antes no dicionário
    elif escolha == "3":
        busca = input("Digite o nome para buscar: ")
        
        for item in contatos:
            if busca.lower() == item["nome"].lower() or busca == item["telefone"] or busca == item["email"]:
                print("Encontrado:")
                print(item)
            else:
                print("Contato não encontrado!")
    #Fechando o programa
    elif escolha == "0":
        print("Saindo...")    
        break    

    else:
        print("Opção inexistente!")





    








    
