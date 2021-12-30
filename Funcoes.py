def perguntar():
    return input("O que deseja realizar?\n" +
                 "<I> _ Para inserir usu�rio\n" +
                 "<P> _ Para Pesquisar um usu�rio\n" +
                 "<E> _ Para Excluir um usu�rio\n" +
                 "<L> _ Para Listar um usu�rio: ").upper()

def inserir(dicionario):
    dicionario[input("Digite o loguin: ").upper()] = [input("Digite o nome: ").upper(),
                                                      input("Digite a �ltima data de acesso: "),
                                                      input("Qual a �ltima esta��o acessada: ").upper()]
    salvar(dicionario)

def salvar(dicionario):
    with open("bd.txt", "a") as arquivo:
        for chave, valor in dicionario.items():
            arquivo.write(chave + ":" + str(valor))