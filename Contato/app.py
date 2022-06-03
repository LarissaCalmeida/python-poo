from contato import Contato 

def menu():
    print("\n============================")
    print("     LISTA DE CONTATOS      ")
    print("============================\n")

    print("1 - Adicionar contato")
    print("2 - Ver lista de contatos")
    print("3 - Sair\n")

def main():
    executando = True

    while(executando):
        menu()

        escolha = int(input("O que deseja fazer (1 - 3): "))

        if(escolha == 1):
            addContact()

        elif(escolha == 2):
            readFile()

        elif(escolha == 3):
            executando = exit()
        

def readFile():
    file = open('./Contato/contact.txt', 'r')
    content = file.read()

    print('\n' + content)

    file.close()

def addContact():
    file = open('./Contato/contact.txt', 'a')
    contato = Contato("", "", "")
    
    nome = input("Nome: ")
    contato.setNome(nome)
    
    email = input("E-mail : ")
    contato.setEmail(email)
    if(not contato.validarEmail()):
        while(not contato.validarEmail()):
            email = input("Digite um e-mail válido: ")
            contato.setEmail(email)
    
    telefone = input("Telefone (DDD) XXXXX-XXXX: ")
    contato.setTelefone(telefone)
    
    if(not contato.validarTelefone()):
        while(not contato.validarTelefone()):
            telefone = input("Digite um telefone válido: ")
            contato.setTelefone(telefone)

    file.write("Nome: " + contato.getNome() + "\n")
    file.write("E-mail: " + contato.getEmail() + "\n")
    file.write("Telefone: " + contato.getTelefone() + "\n\n")
    
    file.close()

def exit():
    continuar = input("Deseja realmente sair (y/n)? ")

    if(continuar == "n"):
        return True

    return False

main()