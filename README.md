# iniciacao_cientifica.exec

### Esse repositório é destinado as contruções feitas no processo de pesquisa da minha Iniciação Cientifica

# Algoritmos de Grafos: Dijkstra e MPA (Busca de Todos os Caminhos)

Este repositório contém duas implementações para trabalhar com grafos:
1. **Algoritmo de Dijkstra**: Encontra o caminho de menor custo entre dois nós em grafos com pesos não negativos.
2. **Algoritmo MPA (Busca de Todos os Caminhos)**: Encontra todos os caminhos possíveis entre dois nós, evitando ciclos.

---

## 📌 Algoritmo de Dijkstra

### **Propósito**
Encontrar o caminho de menor custo (distância) entre dois nós em um grafo direcionado com pesos **não negativos**. Aplicável em redes de transporte, roteamento de redes e otimização de rotas.

### **Estrutura do Código**
- **Grafo**: Representado por nós (inteiros) e arestas (tuplas `(origem, destino, peso)`).
- **Funções**:
  - `obter_arestas(no_atual)`: Filtra arestas que partem de um nó.
  - `reconstruir_caminho(predecessores, origem, destino)`: Reconstrói o caminho mais curto.
  - `dijkstra()`: Implementa o algoritmo principal.

### **Exemplo de Uso**
```python
arestas = [
    (5, 4, 5), (5, 3, 10), (5, 6, 4),
    (4, 3, 2), (4, 1, 2), (6, 4, 1),
    (6, 1, 5), (3, 1, 1), (3, 2, 3), (1, 2, 2)
]
dijkstra()  # Insira origem=5 e destino=2
```

#### **Saída**:
```
Custo total: 10
Caminho: 5 -> 4 -> 3 -> 2
```

### **Diagrama do Grafo**
```
       (5)
      / | \
  5 /   |10 \4
  /     |   \
(4)----(3)  (6)
 | \2 1/ \3  |1
2|  \ /   \  |5
 |   (1)---(2)
 |     \ 2  /
 |5     \  /
(6)-----(1)
     5
```

---

## 📌 Algoritmo MPA (Busca de Todos os Caminhos)

### **Propósito**
Encontrar **todos os caminhos possíveis** entre dois nós em um grafo direcionado, evitando ciclos. Utiliza busca em profundidade (DFS) com backtracking.

### **Estrutura do Código**
- **Grafo**: Representado por uma lista de nós (`S`) e uma matriz de adjacência (`B`).
- **Funções**:
  - `MPA(S, B, start, end)`: Inicia a busca.
  - `search(origin, Q, B, end, caminhos)`: Função recursiva com backtracking.

### **Exemplo de Uso**
```python
S = [1, 2, 3, 4, 5, 6, 7]
B = [
    [2, 3], [3, 4], [6, 0],
    [5, 7], [3, 7], [7, 0], [0, 0]
]
caminhos = MPA(S, B, start=1, end=7)
```

#### **Saída**:
```
Caminhos encontrados:
[1, 2, 3, 6, 7]
[1, 2, 4, 5, 3, 6, 7]
[1, 2, 4, 5, 7]
[1, 2, 4, 7]
[1, 3, 6, 7]
```

### **Funcionamento**
- **Grafo Correspondente**:
  ```
  1 → 2, 3
  2 → 3, 4
  3 → 6
  4 → 5, 7
  5 → 3, 7
  6 → 7
  ```

---

## 🛠️ Como Executar
1. **Clone o repositório**:
   ```bash
   git clone https://github.com/seu-usuario/algoritmos-grafos.git
   cd algoritmos-grafos
   ```

2. **Execute os algoritmos**:
   - **Dijkstra**:
     ```python
     python dijkstra.py
     ```
   - **MPA**:
     ```python
     python mpa.py
     ```

---

## 📝 Considerações Técnicas

| **Característica**       | **Dijkstra**                          | **MPA**                              |
|--------------------------|---------------------------------------|--------------------------------------|
| **Complexidade**         | O((V + E) log V)                      | O(V + E)                             |
| **Pesos**                | Não negativos                         | Não aplicável                        |
| **Saída**                | Caminho único de menor custo          | Todos os caminhos possíveis          |
| **Casos de Uso**         | Rotas ótimas, redes logísticas        | Análise de redes, testes de caminhos |
