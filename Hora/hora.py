class Hora:
    def __init__(self, hora = 0, minuto = 0, segundo = 0, outraHora = None, qtdHora = 0, qtdMinuto = 0, qtdSegundo = 0):
        if(outraHora != None):
            self.__hora = outraHora.__hora
            self.__minuto = outraHora.__minuto
            self.__segundo = outraHora.__segundo

            if(qtdHora != 0 or qtdMinuto != 0 or qtdSegundo != 0):
                segAux = self.__horaEmSeg(qtdHora, qtdMinuto, qtdSegundo)
                self.adiantaEmSegundo(segAux)
        else:
            self.__hora = hora
            self.__minuto = minuto
            self.__segundo = segundo

    def mudarHoraPara(self, hora = 0, minuto = 0, segundo = 0, outraHora = None, qtdHora = 0, qtdMinuto = 0, qtdSegundo = 0):
        if(outraHora != None):
            self.__hora = outraHora.__hora
            self.__minuto = outraHora.__minuto
            self.__segundo = outraHora.__segundo

            if(qtdHora != 0 or qtdMinuto != 0 or qtdSegundo != 0):
                segAux = self.__horaEmSeg(qtdHora, qtdMinuto, qtdSegundo)
                self.adiantaEmSegundo(segAux)
        else:
            self.__hora = hora
            self.__minuto = minuto
            self.__segundo = segundo

    def setHora(self, hora, minuto, segundo):
        self.__hora = hora
        self.__minuto = minuto
        self.__segundo = segundo

        if(not self.__verificarHora()):
            self.__hora = 0
            self.__minuto = 0
            self.__segundo = 0

    def formatHora(self, horario):
        [hora, minuto, segundo] = horario.split(':')

        hora = int(hora)
        minuto = int(minuto)
        segundo = int(segundo)

        self.setHora(hora, minuto, segundo)
    
    def getHora(self):
        hora = str(self.__hora) + ":" + str(self.__minuto)
        return hora

    def getHoraPrecisa(self):
        hora = str(self.__hora) + ":" + str(self.__minuto) + ":" + str(self.__segundo)
        return hora

    def __verificarHora(self):
        if((self.__hora < 0 | self.__hora > 24) | (self.__minuto < 0 | self.__minuto > 59) | (self.__segundo < 0 | self.__segundo > 59)):
            return False

        return True

    def eAm(self):
        if((self.__hora == 12 and self.__minuto == 0 and self.__segundo == 0) or (self.__hora < 12)):
            return True

        return False

        
    def cronometra(self, outraHora):
        [hora, minuto, segundo] = outraHora.split(':')

        hora = int(hora)
        minuto = int(minuto)
        segundo = int(segundo)

        totalSegAux = self.__horaEmSeg(hora, minuto, segundo)
        totalSeg = self.__horaEmSeg(self.__hora, self.__minuto, self.__segundo)
        
        if(totalSegAux >= totalSeg):
            return totalSegAux - totalSeg
        else:
            return totalSeg - totalSegAux + (24 * 3600)

    def __horaEmSeg(self, hora, minuto, segundo):
        return hora * 3600 + minuto * 60 + segundo

    def adiantaEmSegundo(self, segundo):
        totalSeg = self.__horaEmSeg(self.__hora, self.__minuto, self.__segundo) + segundo

        h = totalSeg // 3600
        m = (totalSeg - (h * 3600)) // 60
        s = (totalSeg - (h * 3600) - (m * 60)) % 60

        self.setHora(h, m, s)

