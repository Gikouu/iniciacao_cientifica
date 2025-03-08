import heapq

# Dados do grafo (nós e arestas)
nos = [1, 2, 3, 4, 5, 6]
arestas = [
    (5, 4, 5), (5, 3, 10), (5, 6, 4), (4, 3, 2), (4, 1, 2),
    (6, 4, 1), (6, 1, 5), (3, 1, 1), (3, 2, 3), (1, 2, 2)
]

def obter_arestas(no_atual):
    """Filtra arestas que partem do nó atual usando compreensão de lista."""
    return [(u, v, d) for u, v, d in arestas if u == no_atual]

def reconstruir_caminho(predecessores, origem, destino):
    """Reconstrói o caminho usando um dicionário de predecessores."""
    caminho = []
    atual = destino
    
    if destino not in predecessores and destino != origem:
        raise ValueError("Destino inalcançável.")
    
    while atual != origem:
        caminho.append(atual)
        atual = predecessores[atual]
    caminho.append(origem)
    return caminho[::-1]  # Inverte para ordem origem -> destino

def dijkstra():
    origem = int(input("Digite o nó de origem: "))
    destino = int(input("Digite o nó de destino: "))
    
    # Inicialização das estruturas
    distancias = {no: float('inf') for no in nos}
    distancias[origem] = 0
    predecessores = {}
    visitados = set()
    
    # Fila de prioridade (distância, nó)
    fila = [(0, origem)]
    
    while fila:
        dist_atual, no_atual = heapq.heappop(fila)
        
        if no_atual in visitados:
            continue
        visitados.add(no_atual)
        
        # Parada antecipada se o destino for alcançado
        if no_atual == destino:
            break
        
        # Processa cada aresta do nó atual
        for u, v, distancia in obter_arestas(no_atual):
            if v in visitados:
                continue
            nova_distancia = dist_atual + distancia
            if nova_distancia < distancias[v]:
                distancias[v] = nova_distancia
                predecessores[v] = u
                heapq.heappush(fila, (nova_distancia, v))
    
    # Verifica se o destino é alcançável
    if distancias[destino] == float('inf'):
        print("Não há caminho entre os nós selecionados.")
        return
    
    # Reconstrói e exibe o caminho
    caminho = reconstruir_caminho(predecessores, origem, destino)
    print(f"Custo total: {distancias[destino]}")
    print(f"Caminho: {' -> '.join(map(str, caminho))}")

if __name__ == "__main__":
    dijkstra()