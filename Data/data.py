from math import floor
from datetime import date

class Data:
    def __init__(self, dia = 0, mes = 0, ano = 0, outraData = None, qtdDias = 0):
        if(outraData != None):
            self.__dia = outraData.__dia
            self.__mes = outraData.__mes
            self.__ano = outraData.__ano

            if(qtdDias != 0):
                self.__adiantaDias(qtdDias)
        else:
            self.__dia = dia
            self.__mes = mes
            self.__ano = ano

        if(not self.__verificarData()):
            self.__dia = 0
            self.__mes = 0
            self.__ano = 0

    @staticmethod
    def getDateToday():
        data = date.today()
        print(data.strftime("%d/%m/%Y"))

    def mudarDataPara(self, dia = 0, mes = 0, ano = 0, outraData = None, qtdDias = 0):
        if(outraData != None):
            self.__dia = outraData.__dia
            self.__mes = outraData.__mes
            self.__ano = outraData.__ano

        elif(qtdDias != 0):
            self.__adiantaDias(qtdDias)

        else:
            self.__dia = dia
            self.__mes = mes
            self.__ano = ano
    
    def __adiantaDias(self, adianta):
        qtdDias = self.__diaMes

        for _ in range(adianta + 1):
            if(self.__dia == qtdDias):
                if(self.__mes == 12):
                    self.__ano += 1
                else:
                    self.__mes += 1
            else:
                self.__dia += 1

    def __verificarData(self):
        if(self.__dia < 1 or self.__dia > 31):
            return False
        elif(self.__mes < 1 or self.__mes > 12):
            return False

        return True

    def formatData(self, data):
        [dia, mes, ano] = data.split("/")
        
        dia = int(dia)
        mes = int(mes)
        ano = int(ano)

        self.setData(dia, mes, ano)

    def dateString(self):
        mes = ("janeiro", "feveiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", 
               "outubro", "novembro", "dezembro")

        date = str(self.__dia) + " de " + str(mes[self.__mes - 1]) + " de " + str(self.__ano)

        return date

    def setData(self, dia, mes, ano):
        self.__dia = dia
        self.__mes = mes
        self.__ano = ano

        if(not self.__verificarData()):
            self.__dia = 0
            self.__mes = 0
            self.__ano = 0
            self.__data = str(00) + "/" + str(00) + "/" + str(00)

    def setDia(self, dia):
        self.__dia = dia

        if(not self.__verificarData(self)):
            self.__dia = 0

    def setMes(self, mes):
        self.__mes = mes

        if(not self.__verificarData(self)):
            self.__mes = 0

    def setAno(self, ano):
        self.__ano = ano

        if(not self.__verificarData(self)):
            self.__ano = 0

    def getData(self):
        return self.__data

    def getDia(self):
        return self.__dia

    def getMes(self):
        return self.__mes

    def getAno(self):
        return self.__ano

    def eAnterior(self, data):
        if(self.quantosDiasAte(data) < 0):
            return True
        
        return False

    def quantosDiasAte(self, data):
        [outroDia, outroMes, outroAno] = data.split('/')
        totalDia = 0

        dia = self.getDia()
        mes = self.getMes()
        ano = self.getAno()

        outroDia = int(outroDia)
        outroMes = int(outroMes)
        outroAno = int(outroAno)

        if(ano <= outroAno):
            totalDia += outroDia - dia
    
            for n in range(ano, outroAno):
                totalDia += self.__diaAno(n)
            
            if(mes < outroMes):
                for n in range(mes, outroMes):
                    totalDia += self.__diaMes(n, ano)

            elif(mes > outroMes):
                for n in range(outroMes, mes):
                    totalDia -= self.__diaMes(n, ano)

            return totalDia

        else:
            totalDia += dia - outroDia

            for n in range(outroAno, ano):
                totalDia += self.__diaAno(n)

            if(outroMes < mes):
                for n in range(outroMes, mes):
                    totalDia += self.__diaMes(n, outroAno)

            elif(outroMes > mes):
                for n in range(mes, outroMes):
                    totalDia -= self.__diaMes(n, outroAno)

            return -totalDia

    def __eBissexto(self, ano):
        if(ano % 4 == 0):
            return True

        return False

    def __diaAno(self, ano):
        if(self.__eBissexto(ano)):
            return 366
        else:
            return 365

    def __diaMes(self, mes, ano):
        if((mes == 2) and (self.__eBissexto(ano))):
            return 29

        elif(mes == 2):
            return 28

        elif((mes % 2 != 0 and mes <= 7) or (mes % 2 == 0 and mes > 7)):
            return 31

        else: 
            return 30

    def qualDiaDaSemana(self):
        semana = ("sábado", "domingo", "segunda-feira", "terça-feira", "quarta-feira", "quinta-feira", 
                  "sexta-feira")
        dia = self.__dia
        mes = self.__mes
        ano = self.__ano

        if(dia < 3):
            mes += 12
            ano -= 1

        aux = dia + (2 * mes) + ((3 * (mes + 1 )) / 5) + ano + (ano / 4) - (ano / 100) + (ano / 400) + 2
        diaDaSemana = floor(aux % 7)

        return semana[diaDaSemana]
