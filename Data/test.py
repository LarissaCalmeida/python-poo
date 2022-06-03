from data import Data as date

data = date()

data.setData(7, 5, 2022)

quantosDias = data.quantosDiasAte("07/05/2023")

if(quantosDias > 0):
    print("Faltam {} dias" .format(quantosDias))
else:
    print("Se passaram {} dias" .format(quantosDias * (-1)))

print("Dia da semana: {}" .format(data.qualDiaDaSemana()))
print("É anterior: {}" .format(data.eAnterior("07/05/2023")))

data.getDateToday()