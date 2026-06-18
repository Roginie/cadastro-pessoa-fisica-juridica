from datetime import date


class Endereco:
    def __init__(self, logradouro="", numero="", enderecoComercial=False):
        self.logradouro = logradouro
        self.numero = numero
        self.enderecoComercial = enderecoComercial


class Pessoa:
    def __init__(self, nome="", rendimento=0.0, endereco=None):
        self.nome = nome
        self.rendimento = rendimento
        self.endereco = endereco if endereco is not None else Endereco()

    def calcularImposto(self, rendimento: float) -> float:
        """Metodo base. Cada tipo de pessoa implementa sua propria regra."""
        return 0.0


class PessoaFisica(Pessoa):
    def __init__(self, nome="", rendimento=0.0, endereco=None, cpf="", dataNascimento=None):
        super().__init__(nome, rendimento, endereco)
        self.cpf = cpf
        self.dataNascimento = dataNascimento if dataNascimento is not None else date.today()

    def calcularImposto(self, rendimento: float) -> float:
        if rendimento <= 10500:
            return 0.0
        elif rendimento <= 30500:
            return (rendimento / 100) * 5
        elif rendimento <= 60000:
            return (rendimento / 100) * 8
        else:
            return (rendimento / 100) * 12


class PessoaJuridica(Pessoa):
    def __init__(self, nome="", rendimento=0.0, endereco=None, cnpj="", dataNascimento=None):
        super().__init__(nome, rendimento, endereco)
        self.cnpj = cnpj
        self.dataNascimento = dataNascimento if dataNascimento is not None else date.today()

    def calcularImposto(self, rendimento: float) -> float:
        if rendimento <= 1500:
            return 0.0
        elif rendimento <= 3500:
            return (rendimento / 100) * 2
        elif rendimento <= 6000:
            return (rendimento / 100) * 3.5
        else:
            return (rendimento / 100) * 5
