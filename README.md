# Cadastro de Pessoa Física e Jurídica

Sistema de cadastro em Python aplicando **Programação Orientada a Objetos (POO)**: herança, encapsulamento e polimorfismo. Permite cadastrar, listar, atualizar e remover Pessoas Físicas e Jurídicas, calculando o imposto devido conforme a faixa de rendimento.

## Tecnologias
- Python 3

## Estrutura
| Arquivo | Descrição |
|---------|-----------|
| `Pessoa.py` | Classes `Endereco`, `Pessoa` (base), `PessoaFisica` e `PessoaJuridica` |
| `sistema.py` | Menu interativo no terminal (CRUD completo) |

## Funcionalidades
- Cadastro de Pessoa Física (com validação de maioridade) e Jurídica
- Cálculo de imposto por faixa de rendimento (regras distintas para PF e PJ)
- Listagem, atualização (busca por CPF/CNPJ) e remoção de cadastros
- Validação de entradas inválidas

## Como executar
```bash
python sistema.py
```
