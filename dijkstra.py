#Algoritmo de Dijkstra

nos = [1 ,2 ,3 ,4 ,5 ,6 ]
arestas = [(5, 4, 5), (5, 3, 10), (5, 6, 4), (4, 3, 2), (4, 1, 2)
           , (6, 4, 1), (6, 1, 5), (3, 1, 1), (3, 2, 3), (1, 2, 2)]

def obter_arestas(arestas, ultimo_rotulo):
    index = 0
    arestas_sep = []

    for u, v, distancia in arestas:
        if (u == ultimo_rotulo):
            arestas_sep.append(arestas[index])
            index += 1
        else:
            index += 1

    return arestas_sep

def caminho_minimo(predecessor, origem, destino):

    caminho_correto = []

    while destino != origem:
        for i in range(0,len(predecessor)):
            if predecessor[i][1] == destino:
                caminho_correto.append(predecessor[i])
                destino = predecessor[i][0]


    return caminho_correto


def Dijkstra():

    origem = int(input("Digite o nó de origem: "))
    destino = int(input("Digite o nó de destino: "))
    custo_total = 0
    predecessor = []
    custo_caminhos = []
    ultimo_rotulo = origem

    while ultimo_rotulo != destino:

        caminhos = obter_arestas(arestas, ultimo_rotulo)
        menor = caminhos[0][2]
        nó = caminhos[0][1]

        for i in range(0,len(caminhos)):
            
            custo = min(caminhos[i][2], (custo_total + caminhos[i][2]))
            caminho = ultimo_rotulo, 
            if custo <= menor:
                menor = custo
                nó = caminhos[i][1]
                caminho = ultimo_rotulo, nó
                predecessor.append(caminho)

        custo_total += menor
        ultimo_rotulo = nó
        custo_caminhos.append(menor)
    
    caminho_correto = caminho_minimo(predecessor, origem, destino)

    print(f"O custo total do caminho foi {custo_total}, e seu caminho foi dado por:"
          f"{' -> '.join(str(i) for i in caminho_correto[::-1])}"
    )

    return custo_caminhos, predecessor, custo_total

if __name__ ==  "__main__":
    Dijkstra()

