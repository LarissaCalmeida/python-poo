class Contador:
    def __init__(self, value):
        self.__value = value

    def incrementa(self, incrementa = 1):
        self.__value += incrementa

    def decrementa(self, decrementa = 1):
        self.__value -= decrementa

    def menorQue(self, value):
        return self.__value < value

    def maiorQue(self, value):
        return self.__value > value

    def menorOuIgualQue(self, value):
        return  self.__value <= value

    def maiorOuIgualQue(self, value):
        return self.__value >= value

    def igualA(self, value):
        return self.__value == value

    def diferenteDe(self, value):
        return self.__value != value