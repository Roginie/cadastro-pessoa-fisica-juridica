from datetime import date, datetime
from Pessoa import Endereco, PessoaFisica, PessoaJuridica


def ler_inteiro(mensagem):
    """Le um inteiro do usuario, repetindo ate receber um valor valido."""
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("Valor invalido! Digite um numero inteiro.")


def ler_float(mensagem):
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("Valor invalido! Digite um numero (use ponto para decimais).")


def ler_data(mensagem):
    while True:
        try:
            return datetime.strptime(input(mensagem), '%d/%m/%Y').date()
        except ValueError:
            print("Data invalida! Use o formato dd/mm/aaaa.")


def ler_endereco():
    endereco = Endereco()
    endereco.logradouro = input("Digite o Logradouro: ")
    endereco.numero = input("Digite o numero: ")
    endereco.enderecoComercial = input("Esse endereco e comercial? (S/N): ").strip().upper() == "S"
    return endereco


def calcular_idade(data_nascimento):
    return (date.today() - data_nascimento).days // 365


def imprimir_pessoa(pessoa, documento_label, documento_valor):
    print()
    print(f"Nome: {pessoa.nome}")
    print(f"{documento_label}: {documento_valor}")
    print(f"Endereco: {pessoa.endereco.logradouro}, N: {pessoa.endereco.numero}")
    print(f"Data Nascimento: {pessoa.dataNascimento.strftime('%d/%m/%Y')}")
    print(f"Imposto a ser pago: {pessoa.calcularImposto(pessoa.rendimento):.2f}")


def menu_pessoa_fisica(listaPF):
    while True:
        opcao = ler_inteiro(
            "\nPessoa Fisica - 1: Cadastrar / 2: Listar / 3: Remover / 4: Atualizar / 0: Voltar: "
        )

        if opcao == 1:
            novaPF = PessoaFisica()
            novaPF.nome = input("Digite o nome da Pessoa Fisica: ")
            novaPF.cpf = input("Digite o cpf da Pessoa Fisica: ")
            novaPF.rendimento = ler_float("Digite o rendimento mensal (SOMENTE NUMEROS): ")
            novaPF.dataNascimento = ler_data("Digite a data de nascimento (dd/mm/aaaa): ")

            if calcular_idade(novaPF.dataNascimento) < 18:
                print("Pessoa Fisica tem menos de 18 anos. Cadastro cancelado.")
                continue

            novaPF.endereco = ler_endereco()
            listaPF.append(novaPF)
            print("Cadastro realizado com sucesso!")

        elif opcao == 2:
            if not listaPF:
                print("Lista vazia!")
            for pf in listaPF:
                imprimir_pessoa(pf, "CPF", pf.cpf)

        elif opcao == 3:
            cpf = input("Digite o cpf da Pessoa Fisica que sera excluida: ")
            encontrada = next((p for p in listaPF if p.cpf == cpf), None)
            if encontrada:
                listaPF.remove(encontrada)
                print("Pessoa fisica removida.")
            else:
                print("Nenhuma pessoa encontrada.")

        elif opcao == 4:
            cpf = input("Digite o cpf da Pessoa Fisica que sera atualizada: ")
            pessoa = next((p for p in listaPF if p.cpf == cpf), None)
            if not pessoa:
                print("Nenhuma pessoa encontrada.")
                continue
            campo = ler_inteiro("Atualizar: 1: Nome / 2: Endereco / 3: Data Nascimento / 4: Rendimento: ")
            if campo == 1:
                pessoa.nome = input("Digite o novo nome: ")
            elif campo == 2:
                pessoa.endereco = ler_endereco()
            elif campo == 3:
                pessoa.dataNascimento = ler_data("Digite a nova data de nascimento (dd/mm/aaaa): ")
            elif campo == 4:
                pessoa.rendimento = ler_float("Digite o novo rendimento mensal: ")
            else:
                print("Opcao invalida.")
                continue
            print("Atualizado com sucesso!")

        elif opcao == 0:
            break
        else:
            print("Opcao invalida! Digite uma das opcoes indicadas.")


def menu_pessoa_juridica(listaJ):
    while True:
        opcao = ler_inteiro(
            "\nPessoa Juridica - 1: Cadastrar / 2: Listar / 3: Remover / 4: Atualizar / 0: Voltar: "
        )

        if opcao == 1:
            novaJ = PessoaJuridica()
            novaJ.nome = input("Digite o nome da Pessoa Juridica: ")
            novaJ.cnpj = input("Digite o cnpj da Pessoa Juridica: ")
            novaJ.rendimento = ler_float("Digite o rendimento mensal (SOMENTE NUMEROS): ")
            novaJ.dataNascimento = ler_data("Digite a data de abertura (dd/mm/aaaa): ")
            novaJ.endereco = ler_endereco()
            listaJ.append(novaJ)
            print("Cadastro realizado com sucesso!")

        elif opcao == 2:
            if not listaJ:
                print("Lista vazia!")
            for pj in listaJ:
                imprimir_pessoa(pj, "CNPJ", pj.cnpj)

        elif opcao == 3:
            cnpj = input("Digite o cnpj da Pessoa Juridica que sera excluida: ")
            encontrada = next((p for p in listaJ if p.cnpj == cnpj), None)
            if encontrada:
                listaJ.remove(encontrada)
                print("Pessoa juridica removida.")
            else:
                print("Nenhuma pessoa encontrada.")

        elif opcao == 4:
            cnpj = input("Digite o cnpj da Pessoa Juridica que sera atualizada: ")
            pessoa = next((p for p in listaJ if p.cnpj == cnpj), None)
            if not pessoa:
                print("Nenhuma pessoa encontrada.")
                continue
            campo = ler_inteiro("Atualizar: 1: Nome / 2: Endereco / 3: Data Abertura / 4: Rendimento: ")
            if campo == 1:
                pessoa.nome = input("Digite o novo nome: ")
            elif campo == 2:
                pessoa.endereco = ler_endereco()
            elif campo == 3:
                pessoa.dataNascimento = ler_data("Digite a nova data de abertura (dd/mm/aaaa): ")
            elif campo == 4:
                pessoa.rendimento = ler_float("Digite o novo rendimento mensal: ")
            else:
                print("Opcao invalida.")
                continue
            print("Atualizado com sucesso!")

        elif opcao == 0:
            break
        else:
            print("Opcao invalida! Digite uma das opcoes indicadas.")


def main():
    listaPF = []
    listaJ = []
    while True:
        opcao = ler_inteiro("\nMenu Principal - 1: Pessoa Fisica / 2: Pessoa Juridica / 0: Sair: ")
        if opcao == 1:
            menu_pessoa_fisica(listaPF)
        elif opcao == 2:
            menu_pessoa_juridica(listaJ)
        elif opcao == 0:
            print("Obrigado por utilizar o nosso sistema!")
            break
        else:
            print("Opcao invalida! Por favor digite uma das opcoes validas.")


if __name__ == "__main__":
    main()
