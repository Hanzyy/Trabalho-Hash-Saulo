def criar_tabela():     #Caso queira mudar o tamanho da tabela, pode apenas colocar um parâmetro para a função
    tabela = []     #Cria uma matriz vazia
    estado = []     #Cria a linha de estados da tabela
    nomes = []      #Cria a linha onde ficaram os nomes
    for i in range(8):
        estado.append("L")      #Coloca 8 colunas com a string L, indicando que todos os espaços estão livres
        nomes.append("")        #Coloca 8 colunas vazias
    tabela.append(estado)       #Coloca a linha de estados na primeira linha
    tabela.append(nomes)        #Coloca a linha de nomes na segunda linha
    return tabela


def funcao_hash(nome, tamanho_tabela):
    lista = []      #Cria uma lista vazia
    for char in nome:
        lista.append(ord(char))     #Coloca os valores de cada caracter do nome em uma lista, já convertido em valores da tabela ACSII
    a = sum(lista)      #Faz a soma de cada valor da lista
    pos_tabela = a%tamanho_tabela       #Acha o valor da posição da matriz que o nome ficará
    return pos_tabela


def inserir(tabela, nome):
    tamanho = len(tabela[1])        #Verifica o tamanho da tabela, mas como é um valor padrão, será 8
    lugar = funcao_hash(nome, tamanho)      #Chama a funcao_hash para descobrir a posição do nome
    print(f"\nNome: {nome}")
    print(f"Lugar = {lugar}")
    if tabela[0][lugar] == 'L' or tabela[0][lugar] == 'R':      #Se o lugar estiver com o estado de Livre (L) ou Deletado (R)
        tabela[1][lugar] = nome                                 #Coloca o nome na posição
        tabela[0][lugar] = 'O'                                  #Muda o estado da posição para Ocupado (O)
        print("Lugar vazio")
        print(tabela)
        return tabela
    else:                           #Se o lugar estiver Ocupado
        b = 1                       #Inicializa uma váriavel para manter controle das tentativas
        print("Lugar ocupado\n")
        while b < tamanho:                          #Enquanto a variável for menor que o tamanho, ou seja, chegar a 7 tentativas
            lugar = (lugar + b*b) % tamanho         #Tentativa quadrática
            print(f"Tentativa = {b}")                       #Identifica o número da tentativa
            print(f"Novo lugar = {lugar}")          #Identifica qual o novo lugar o qual será colocado
            if tabela[0][lugar] == 'L' or tabela[0][lugar] == 'R':      #Se o lugar estiver com o estado de Livre (L) ou Deletado(R)
                tabela[1][lugar] = nome                                 #Coloca o nome na posição
                tabela[0][lugar] = 'O'                                  #Muda o estado da posição para Ocupado (O)
                print("Lugar vazio")
                print(tabela)
                return tabela
            else:                           #Se o lugar estiver Ocupado
                print("Lugar ocupado\n")
                b += 1                      #Passa para próxima tentativa
        if b == len(tabela[1]):             #Se passar para a 8ª tentativa
            print("\nTabela cheia\n")           #Indica que a tabela está cheia
            return tabela



def buscar(tabela, nome):
    tamanho = len(tabela[1])        #Verifica o tamanho da tabela, mas como é um valor padrão, será 8
    a = 0                           #Inicia uma variável para a verificação de cada posição
    while a < tamanho:              #Enquanto a variável for menor que o tamanho da matriz
        if tabela[1][a] == nome:                                #Se o nome estiver naquela posição
            print(f"Nome encontrado na posição [1][{a}]")       #Mostra em qual posição da matriz o nome está
            return a                                            #Retorna a posição da matriz
        a+=1                        #Passa para próxima tentativa
    print("Nome não encontrado na tabela")          #Se passar por todas as posições e não achar o nome
    return None                                     #Retorna None


def deletar(tabela, nome):
    a = buscar(tabela, nome)             #Faz a busca na matriz para descobrir qual posição está
    if a != None:                        #Se achar alguma posição onde não seja None
        tabela[1][a] = ""                #Deleta o nome
        tabela[0][a] = "R"               #Muda o estado para Deletado (R)


def registrar_nomes(filename):
    with open(filename, "r") as file:       #Abre o arquivo proposto
        for linha in file:                  #Para cada linha no arquivo
            data = linha.split()            #Separa cada nome no arquivo
        return data                         #Retorna um vetor com todos os nomes do arquivo, separadamente


def inserir_varios_nomes(tabela, nomes):
    i = 0                                   #Inicia uma variável para contar as posições do vetor
    while i < len(nomes):                   #Para cada posição do vetor lido pelo arquivo
        inserir(tabela, nomes[i])           #Faz a chamada da função inserir várias vezes
        i += 1
    return tabela




if __name__ == "__main__":

    print("Criando a tabela")
    tabela = criar_tabela()
    print("Tamanho da tabela: 8")
    print(tabela)

    print("\n--------------------------------------------------------------------------------------------------------")
    print("Inserindo vários nomes de uma vez ")
    nomes = registrar_nomes("nomes.txt")
    inserir_varios_nomes(tabela, nomes)

    print("\n--------------------------------------------------------------------------------------------------------")
    print("Buscar na tabela\n")
    print("Cainan:")
    buscar(tabela, "Cainan")
    print("\nDiego:")
    buscar(tabela, "Diego")

    print("\n--------------------------------------------------------------------------------------------------------")
    print("Deletar na tabela\n")

    print(f"{tabela}\n")
    deletar(tabela, "Edu")
    print(tabela)

    print("\n--------------------------------------------------------------------------------------------------------")
    print("Inserir na tabela\n")
    print("Brayan")
    inserir(tabela, "Brayan")