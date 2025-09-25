# A classe Cachorro é o "molde"
class Cachorro:
# O método __init__ é o construtor.
# Ele define as características iniciais (atributos) de cada objeto.
def __init__(self, nome, idade):
# 'self.nome' e 'self.idade' são atributos de instância,
# específicos para cada objeto (cada cachorro).
self.nome = nome
self.idade = idade

