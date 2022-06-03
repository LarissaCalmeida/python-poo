from random import seed
from random import random
import Math

seed(1)

class Array:
    def __init__(self, tamanho):
        self.__tamanho = tamanho

        for n in range(tamanho):
            self.__array[n] = random()

    def soma(self):
        soma = 0

        for n in range(tamanho):
            soma += self.__array[n]

        return soma

    def media(self):
        soma = self.__soma()

        return soma / self.__tamanho

    def maiorElemento(self):
        maior = max(self.__array)

        return maior

    def menorElemento(self):
        menor = min(self.__array)

        return menor

    def getArray(self):
        return self.__array

    def setArray(self, tamanho):
        self.__tamanho = tamanho

        for n in range(tamanho):
            self.__array[n] = random()