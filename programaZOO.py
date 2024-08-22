class Animal:
    def __init__(self,nome,idade,barulho,movimento,alimentacao,habitat,vizinhos,horas_alimentacao):
        self.nome = nome
        self.idade = idade
        self.barulho = barulho
        self.movimento = movimento
        self.alimentacao = alimentacao
        self.habitat = habitat
        self.vizinhos = []
        self.horas_alimentacao = horas_alimentacao

    def alimentar(self):
        return f"{self.nome}  foi alimentado às {self.horas_alimentacao}."
    
    def __str__(self):
        return f"{self.nome}, {self.idade} anos, {self.horas_alimentacao}, Habitat:{self.habitat}"
#fcgfcgfcgfcgfc