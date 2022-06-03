from agendamento import Agendamento

def menu():
    print("\n============================")
    print("         Agendamento         ")
    print("============================\n")

    print("1 - Adicionar evento")
    print("2 - Procurar evento por nome")
    print("3 - Procurar evento por data")
    print("4 - Sair\n")

def main():
    eventos = []
    executando = True
    
    while(executando):
        menu()
        escolha = int(input("O que deseja fazer (1 - 4): "))

        if(escolha == 1):
            addEvent(eventos)

        elif(escolha == 2):

            res = getEventName(eventos)

            if(res == -1):
                print("Evento não encontrado")
            else:
                print("\n")
                res.printInfo()

        elif(escolha == 3):
            res = getEventDate(eventos)

            if(res == -1):
                print("Evento não encontrado")
            else:
                print("\n")
                res.printInfo()


        elif(escolha == 4):
            executando = exit()

def addEvent(event):
    nome = input("Nome do evento: ")
    data = input("Data (dd/mm/yyyy): ")
    hora = input("Hora do evento: ")
    duracao = input("Duração: ")
    participantes = input("Participantes: ")

    agenda = Agendamento(nome, data, hora, duracao, participantes)
    event.append(agenda)

def getEventName(events):
    name = input("Nome do Evento: ")

    for event in events:
        if(name == event.getNome()):
            return event

    return -1
    

def getEventDate(events):
    name = input("Data do Evento (dd/mm/yyyy): ")

    for event in events:
        if(name == event.getData()):
            return event

    return -1

def exit():
    continuar = input("Deseja realmente sair (y/n)? ")

    if(continuar == "n"):
        return True

    return False

main()