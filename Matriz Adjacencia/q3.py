from grafo import Grafo

lista_vertices = []
dict_arestas = {}
vertices_index = {}


def recebe_vertices():
    vertices = input("Digite todos os vértices: ").split(", ")
    return vertices


def recebe_arestas():
    arestas_dict = {}
    while True:
        arestas = input("Digite as arestas: ").split(", ")
        condicao = True
        for i in range(len(arestas)):
            temp = ""
            for j in range(len(arestas[i])):
                if ")" not in arestas[i] or "(" not in arestas[i] or "-" not in arestas[i] or arestas[i][0] == "(":
                    condicao = False
                    break
                elif arestas[i][j] == "(":
                    if arestas[i][j + 3].isalpha():
                        arestas_dict[temp] = arestas[i][j + 1:len(arestas[i][j]) - 2]
                    else:
                        condicao = False
                    break
                elif arestas[i][j] == ")":
                    condicao = False
                    break
                temp += arestas[i][j]

        if not condicao:
            print("Arestas inválidos")
        else:
            return arestas_dict


def vertice_adjacente(matriz):
    for i in range(len(matriz)):
        if matriz[i][i] > 0:
            return True
    return False


def criar_vertices_index():
    vertices_dict = {}
    for i in range(len(lista_vertices)):
        vertices_dict[i] = lista_vertices[i]

    return vertices_dict


def matriz_adjacencia(vertices_dict):
    matriz = []
    for i in range(len(vertices_dict.keys())):
        matriz.append([])
        for j in range(len(vertices_dict.keys())):
            matriz[i].append(lista_aresta.count((vertices_dict[i] + "-" + vertices_dict[j])))

    return matriz


def forma_tabular(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if (j - 1) < len(matriz[i]):
                print(matriz[i][j], end=" ")
            else:
                print(matriz[i][j], end="")
        print("\n")


def vertices_nao_adjacente(matriz, vertices):
    lista_nao_adjacantes = []
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == 0 and vertices[j] + "-" + vertices[i] not in lista_aresta:
                lista_nao_adjacantes.append((vertices[i] + "-" + vertices[j]))

    return lista_nao_adjacantes


def aresta_paralelas(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == 1 and matriz[j][i] == 1 or matriz[i][j] > 1:
                return True
    return False


def arestas_incidem(vertice):
    lista = []
    for i in dict_arestas.keys():
        if vertice in dict_arestas[i]:
            lista.append(i)
    return lista


def grau_vertice(vertice_procurar):
    # So conta de vertice_procurar-vertice_qualquer ou tanto faz
    cont = 0
    try:
        indice = [indice for indice, vertice in vertices_index.items() if vertice == vertice_procurar][0]
    except IndexError:
        return cont

    for i in range(len(lista_vertices)):
        cont += matriz_adjacencia[i][indice]
        cont += matriz_adjacencia[indice][i]
    return cont


def eh_completo(matriz):
    # Em um grafo direcionado, faz diferenca a eu ter A-B mas n B-A
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == 0 and i != j:
                return False
    return True


def criar_arestas_lista():
    lista = []
    for i in dict_arestas.values():
        lista.append(i)
    return lista


def encontra_comprimento(matriz):
    maior_caminho = 0

    for inicio in lista_vertices:
        pilha = [[inicio]]

        while pilha:
            caminhos = pilha.pop(0)
            if maior_caminho < len(caminhos) - 1:
                maior_caminho = len(caminhos) - 1
            indice_vertice = lista_vertices.index(caminhos[-1])
            for indice, vertice in enumerate(lista_vertices):
                if matriz[indice_vertice][indice] != 0 and vertice not in caminhos:
                    pilha.append(caminhos + [vertice])

    return maior_caminho


def main():
    # Copiei o menu msm pq sou preguicoso
    while True:
        print("\na - Encontre todos os pares de vértices não adjacentes.\n"
              "b - Há algum vértice adjacente a ele mesmo?\n"
              "c - Há arestas paralelas?\n"
              "d - Saber o grau de um vertice qualquer.\n"
              "e - Saber as arestas incidentes de um vertice\n"
              "f - Esse grafo é completo?\n"
              "g - Maior caminho nesse grafo.\n"
              "h - Sair do programa.\n")
        escolha = input("Informe uma opção: ").lower()
        if escolha == 'a':
            print(vertices_nao_adjacente(matriz_adjacencia, lista_vertices))
        elif escolha == 'b':
            print(vertice_adjacente(matriz_adjacencia))
        elif escolha == 'c':
            print("Aresta paralelas: " + str(aresta_paralelas(matriz_adjacencia)))
        elif escolha == 'd':
            vertice = input("Qual vertice: ").upper()
            print("Grau do vértice: %d" % grau_vertice(vertice))
        elif escolha == 'e':
            vertice = input("Qual vertice: ").upper()
            print("Arestas que incidem: " + str(arestas_incidem(vertice)))
        elif escolha == 'f':
            print(eh_completo(matriz_adjacencia))
        elif escolha == 'g':
            print(encontra_comprimento(matriz_adjacencia))
        elif escolha == 'h':
            return


while True:
    try:
        lista_vertices = recebe_vertices()
        dict_arestas = recebe_arestas()
        gr = Grafo(lista_vertices, dict_arestas)
        lista_aresta = criar_arestas_lista()
        vertices_index = criar_vertices_index()
        matriz_adjacencia = matriz_adjacencia(vertices_index)
        break
    except:
        print("Arestas ou vértices inválidos")

if __name__ == '__main__':
    main()

# testes
# J, C, E, P, M, T, Z
# a1(J-C), a2(E-C), a3(C-E), a4(C-P), a5(C-C), a6(C-M), a7(C-T), a8(M-T), a9(T-Z)
# J, C, B
# a1(J-C), a2(J-B), a3(C-B)
# a1(J-C), a2(J-B), a3(C-B), a4(J-J), a5(B-B), a6(C-C)
# A, B, C
# a1(A-B), a2(A-A), a3(B-A)