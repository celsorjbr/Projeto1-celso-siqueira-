def perguntar():
    return input("O que deseja realizar?\n" +
                 "<I> _ Para inserir usuário\n" +
                 "<P> _ Para Pesquisar um usuário\n" +
                 "<E> _ Para Excluir um usuário\n" +
                 "<L> _ Para Listar um usuário: ").upper()

def inserir(dicionario):
    dicionario[input("Digite o loguin: ").upper()] = [input("Digite o nome: ").upper(),
                                                      input("Digite a última data de acesso: "),
                                                      input("Qual a última estação acessada: ").upper()]
    salvar(dicionario)

def salvar(dicionario):
    with open("bd.txt", "a") as arquivo:
        for chave, valor in dicionario.items():
            arquivo.write(chave + ":" + str(valor))