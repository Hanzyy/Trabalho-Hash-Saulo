def criar_tabela():
    tabela = []
    estado = []
    nomes = []
    for i in range(8):
        estado.append("L")
        nomes.append("")
    tabela.append(estado)
    tabela.append(nomes)
    return tabela


def funcao_hash(nome, tamanho_tabela):
    lista = []
    for char in nome:
        lista.append(ord(char))
    a = sum(lista)
    pos_tabela = a%tamanho_tabela
    return pos_tabela


def inserir(tabela, nome):
    tamanho = len(tabela[1])
    lugar = funcao_hash(nome, tamanho)
    print(f"Lugar = {lugar}")
    if tabela[0][lugar] == 'L' or tabela[0][lugar] == 'R':
        tabela[1][lugar] = nome
        tabela[0][lugar] = 'O'
        print(tabela)
        return tabela
    else:
        b = 1
        print("Lugar ocupado")
        while b < tamanho:
            lugar = (lugar + b*b) % tamanho
            print(f"b = {b}")
            print(f"Novo lugar = {lugar}")
            if tabela[0][lugar] == 'L' or tabela[0][lugar] == 'R':
                tabela[1][lugar] = nome
                tabela[0][lugar] = 'O'
                print("Lugar vazio")
                print(tabela)
                return tabela
            else:
                print("Lugar ocupado")
                b += 1
        if b == len(tabela[1]):
            print("Tabela cheia")
            return tabela



def buscar(tabela, nome):
    tamanho = len(tabela[1])
    a = 0
    while a < tamanho:
        if tabela[1][a] == nome:
            print(f"Nome encontrado na posição [1][{a}]")
            return a
        a+=1
    print("Nome não encontrado na tabela")
    return None


def deletar(tabela, nome):
    a = buscar(tabela,nome)
    if a != None:
        tabela[1][a] = ""
        tabela[0][a] = "R"


def registrar_nomes(filename):
    with open(filename, "r") as file:
        for linha in file:
            data = linha.split()
        return data


def inserir_varios_nomes(tabela, nomes):
    i = 0
    while i < len(nomes):
        inserir(tabela, nomes[i])
        i += 1
    return tabela




if __name__ == "__main__":

    tabela = criar_tabela()
    print("Tamanho da tabela: 8")
    print(tabela)

    nomes = registrar_nomes("nomes.txt")

    inserir_varios_nomes(tabela, nomes)

    print("\n------------------------------------------------------------")
    print("Buscar na tabela\n")
    buscar(tabela, "Pedro")
    buscar(tabela, "Pedro1")

    print("\n------------------------------------------------------------")
    print("Deletar na tabela\n")
    deletar(tabela, "Edu")
    print(tabela)

    print("\n------------------------------------------------------------")
    print("Inserir na tabela\n")
    inserir(tabela, "Brayan")