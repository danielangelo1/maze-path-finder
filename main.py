import time

from labirinto import Labirinto

def main():
    while True:
        arquivo = input("Informe o arquivo (0 para sair): ")
        if arquivo == '0':
            break

        try:
            labirinto = Labirinto(arquivo)

            # Busca em Largura (BFS)
            inicio_bfs = time.time()
            caminho_bfs = labirinto.busca_em_largura()
            tempo_bfs = time.time() - inicio_bfs
            print("Caminho BFS:", caminho_bfs)
            print("Tempo BFS:", tempo_bfs, "s")

            # Busca em Profundidade (DFS)
            inicio_dfs = time.time()
            caminho_dfs = labirinto.busca_em_profundidade()
            tempo_dfs = time.time() - inicio_dfs
            print("\nCaminho DFS:", caminho_dfs)
            print("Tempo DFS:", tempo_dfs, "s")

        except FileNotFoundError:
            print("Arquivo não encontrado.")

if __name__ == "__main__":
    main()