from collections import deque

class Labirinto:
    def __init__(self, arquivo):
        self.labirinto, self.inicio, self.saida = self.ler_arquivo(arquivo)
        self.linhas = len(self.labirinto)
        self.colunas = len(self.labirinto[0])
        self.visitado = set()
        

    def ler_arquivo(self, arquivo):
        with open(arquivo, 'r') as f:
            labirinto = [list(linha.strip()) for linha in f]

        inicio = None
        saida = None
        for i in range(len(labirinto)):
            for j in range(len(labirinto[0])):
                if labirinto[i][j] == 'S':
                    inicio = (i, j)
                elif labirinto[i][j] == 'E':
                    saida = (i, j)

        return labirinto, inicio, saida

    def busca_em_largura(self):
        fila = deque([(self.inicio, [])])
        visitado = set()  
        visitado.add(self.inicio)

        while fila:
            (i, j), caminho = fila.popleft()
            if (i, j) == self.saida:
                return caminho + [(i, j)]

            for vizinho in self.obter_vizinhos(i, j):
                if vizinho not in visitado:
                    fila.append((vizinho, caminho + [(i, j)]))
                    visitado.add(vizinho) 
        return None  

    def busca_em_profundidade(self, i=None, j=None, caminho=None, visitado=None):
        if i is None and j is None:
            i, j = self.inicio
            caminho = []
            visitado = set()  

        if (i, j) == self.saida:
            return caminho + [(i, j)]

        visitado.add((i, j))
        for vizinho in self.obter_vizinhos(i, j):
            if vizinho not in visitado:
                resultado = self.busca_em_profundidade(*vizinho, caminho + [(i, j)], visitado.copy())  
                if resultado:
                    return resultado

        return None


    def eh_valido(self, i, j):
        return 0 <= i < self.linhas and 0 <= j < self.colunas and self.labirinto[i][j] != '#' 

    def obter_vizinhos(self, i, j):
        vizinhos = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]
        return [(x, y) for x, y in vizinhos if self.eh_valido(x, y)]