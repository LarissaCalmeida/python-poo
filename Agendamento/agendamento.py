class Agendamento:
    def __init__(self, nome, data, horaInicio, duracao, participantes):
        self.__nome = nome
        self.__data = data
        self.__horaInicio = horaInicio
        self.__duracao = duracao
        self.__participantes = participantes

    # Métodos set
    def setAgendamento(self, nome, data, horaInicio, duracao, participantes):
        self.__nome = nome
        self.__data = data
        self.__horaInicio = horaInicio
        self.__duracao = duracao
        self.__participantes = participantes

    def setNome(self, nome):
        self.__nome = nome

    def setData(self, data):
        self.__data = data

    def setHora(self, horaInicio):
        self.__horaInicio = horaInicio

    def setDuracao(self, duracao):
        self.__duracao = duracao

    def setParticipantes(self, participantes):
        self.__participantes = participantes

    # Métodos get
    def getNome(self):
        return self.__nome

    def getData(self):
        return self.__data

    def getHora(self):
        return self.__horaInicio

    def getDuracao(self):
        return self.__duracao

    def getParticipantes(self):
        return self.__participantes

    def printInfo(self):
        print("Nome: " + self.__nome)
        print("Data: " + self.__data)
        print("Hora: " + self.__horaInicio)
        print("Duracao: " + self.__duracao)
        print("Participantes: " + self.__participantes)

    def getInfo(self):
        return ( 
            self.__nome,
            self.__data,
            self.__horaInicio,
            self.__duracao,
            self.__participantes,
        )