from hora import Hora

hora = Hora(12, 59, 00)

# Antes
print(hora.cronometra("11:59:00"))
# Depois
print(hora.cronometra("13:59:00"))
# Verificar se é AM
print(hora.eAm())
# Ver hora atual
print(hora.getHoraPrecisa())
# Adiantar em 60 seg
hora.adiantaEmSegundo(60)
# Ver hora novamente
print(hora.getHoraPrecisa())
