class Medico:

    def __init__(self,nome,idade,especialidade):
        self.nome = nome
        self.idade = idade
        self.especialidade = especialidade

    def apresentar (self):
        print (f"Olá, meu nome é {self.nome} e eu sou {self.especialidade}")

#elisa = Medico('Elisa',26,'pediatra')
#cristiano = Medico('Cristiano', 32, 'cardiologista')

#elisa.apresentar()
#cristiano.apresentar()

class Cirurgiao(Medico):

    def __init__(self, nome,idade,especialidade,valor):
        super().__init__(nome,idade,especialidade)
        self.valor = valor

    def orcamento(self,horas):
        custo = horas * self.valor
        print (f"A cirurgia vai custar R${custo}")

doc = Cirurgiao('Cain',47,'cirurgiao-geral',4000)

doc.orcamento(4)