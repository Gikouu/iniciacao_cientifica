#Algoritmo MPA

def MPA(S, B, start=1, end=7):
    caminhos = []
    Q = [start]
    search(start - 1, Q, B, end, caminhos)
    return caminhos

def search(origin, Q, B, end, caminhos):
    if origin == end - 1:
        caminhos.append(Q.copy())
        return

    for k in range(len(B[0])):
        no = B[origin][k]
        if no == 0:
            continue
        if no not in Q:
            Q.append(no)
            search(no - 1, Q, B, end, caminhos)
            Q.pop()

if __name__ == "__main__":
    S = [1, 2, 3, 4, 5, 6, 7]
    B = [[2, 3], [3, 4], [6, 0], [5, 7], [3, 7], [7, 0], [0, 0]]
    caminhos = MPA(S, B)
    print("Caminhos encontrados")
    for caminho in caminhos:
        print(caminho)