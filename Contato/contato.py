import re 

class Contato:
    totalContato = 0

    

    def __init__(self, nome, email, telefone):
        self.__nome = nome
        self.__email = email
        self.__telefone = telefone
        self.incrementTotalContato()
        
    @staticmethod
    def incrementTotalContato():
        Contato.totalContato += 1

    @staticmethod
    def getTotalContato():
        return Contato.totalContato

    # Métodos set
    def setContato(self, nome, sobrenome, email, telefone):
        self.__nome = Nome(nome, sobrenome)
        self.__email = Email(email)
        self.__telefone = Telefone(telefone)
                

    # Métodos get
    def getContato(self):
        return {
            'nome': self.__nome + " " + self.__sobrenome,
            'email': self.__email,
            'telefone': self.__telefone,
        }

    

class Nome:
    def __init__(self, nome, sobrenome):
        self.__nome = nome
        self.__sobrenome = sobrenome 
    
    def setNome(self, nome):
        self.__nome = nome

    def setSobrenome(self, sobrenome):
        self.__sobrenome = sobrenome

    def setNomeCompleto(self, nome, sobrenome):
        self.__nome = nome
        self.__sobrenome = sobrenome

    def getNome(self):
        return self.__nome

    def getSobrenome(self):
        return self.__sobrenome

    def getNomeCompleto(self):
        return {'nome': self.__nome, 'sobrenome': self.__sobrenome}

class Telefone:
    def __init__(self, telefone):
        self.__telefone = telefone

    def setTelefone(self, telefone):
        self.__telefone = telefone

    def getTelefone(self):
        return self.__telefone

    #Verificação de telefone
    def validarTelefone(self):
        regex = re.compile(r'((?:\+\d{2}[-\.\s]??|\d{4}[-\.\s]??)?(?:\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4}))')

        if(self.__telefone == ""):
            return True

        if(re.fullmatch(regex, self.__telefone)):
            return True
        return False

class Email:

    def __init__(self, email):
        self.__email = email

    def getEmail(self):
        return self.__email

    def setEmail(self, email):
        self.__email = email

    #Verificação de E-mail
    def validarEmail(self):
        regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')

        if(self.__email == ""):
            return True
        
        if(re.fullmatch(regex, self.__email)):
            return True
        return False


    

    

    