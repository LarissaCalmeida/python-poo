from hora import Hora
print("==============================\n")
print("|       Estou atrasado?      |\n")
print("==============================\n")

horarioAux = input("Digite o horario do seu relogio evento (h:m:s): ")
horarioEvento = Hora(0, 0, 0)
horarioEvento.formatHora(horarioAux)

horarioAux = input("Digite o horario do seu relogio (h:m:s): ")
horarioAtual = Hora(0, 0 ,0)
horarioAtual.formatHora(horarioAux)


horaEvento = horarioEvento.getHora().split(":") 
horaAtual = horarioAtual.getHora().split(":")

if((int(horaEvento[0]) <= int(horaAtual[0])) & (int(horaEvento[1]) <= int(horaAtual[1]))):
    print("Estou atrasado")
elif():
    print("Não estou atrasada") 