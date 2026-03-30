contatos = []


while True:
    #Interface do sistema
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
        contatos.append(nome)
        contatos.append(telefone)
        contatos.append(email)      
    
        
        


    








    
