import time
import random

# --- ALGORITMOS DE BUSCA ---

def busca_sequencial(lista, elemento):
    """
    Realiza uma busca sequencial em uma lista.

    Retorna uma tupla contendo a posição do elemento (ou -1 se não encontrado)
    e o número de posições visitadas.
    """
    posicoes_visitadas = 0
    for i, item in enumerate(lista):
        posicoes_visitadas += 1
        if item == elemento:
            return i, posicoes_visitadas
    return -1, posicoes_visitadas

def busca_binaria(lista, elemento):
    """
    Realiza uma busca binária em uma lista ordenada.

    Retorna uma tupla contendo a posição do elemento (ou -1 se não encontrado)
    e o número de posições visitadas.
    """
    inicio, fim = 0, len(lista) - 1
    posicoes_visitadas = 0
    
    while inicio <= fim:
        meio = (inicio + fim) // 2
        posicoes_visitadas += 1
        
        if lista[meio] == elemento:
            return meio, posicoes_visitadas
        elif elemento < lista[meio]:
            fim = meio - 1
        else:
            inicio = meio + 1
            
    return -1, posicoes_visitadas

# --- FUNÇÃO PARA EXECUTAR OS TESTES ---

def executar_testes(tamanhos_entrada):
    """
    Executa os testes de desempenho para busca sequencial e binária
    e imprime os resultados.
    """
    print("Comparação de desempenho: Busca Sequencial vs. Busca Binária")
    print("-" * 80)
    print(f"{'Tamanho Entrada':<18} | {'Tipo de Caso':<15} | {'Algoritmo':<18} | {'Tempo (s)':<15} | {'Posições Visitadas':<20}")
    print("-" * 80)

    for tamanho in tamanhos_entrada:
        # Gera uma lista ordenada de números únicos
        conjunto_dados = sorted(random.sample(range(tamanho * 2), tamanho))
        
        # --- CASO MÉDIO (Elemento em posição aleatória) ---
        elemento_medio = random.choice(conjunto_dados)

        # Teste: Busca Sequencial - Caso Médio
        inicio_tempo = time.perf_counter()
        _, visitadas_seq_medio = busca_sequencial(conjunto_dados, elemento_medio)
        fim_tempo = time.perf_counter()
        tempo_seq_medio = fim_tempo - inicio_tempo
        
        print(f"{tamanho:<18} | {'Caso Médio':<15} | {'Busca Sequencial':<18} | {tempo_seq_medio:<15.6f} | {visitadas_seq_medio:<20}")

        # Teste: Busca Binária - Caso Médio       
        inicio_tempo = time.perf_counter()
        _, visitadas_bin_medio = busca_binaria(conjunto_dados, elemento_medio)
        fim_tempo = time.perf_counter()
        tempo_bin_medio = fim_tempo - inicio_tempo
        
        print(f"{tamanho:<18} | {'Caso Médio':<15} | {'Busca Binária':<18} | {tempo_bin_medio:<15.6f} | {visitadas_bin_medio:<20}")

        # --- PIOR CASO (Elemento não presente) ---
        elemento_pior_caso = tamanho * 2 + 1 # Garante que o elemento não está na lista

        # Teste: Busca Sequencial - Pior Caso
        inicio_tempo = time.perf_counter()
        _, visitadas_seq_pior = busca_sequencial(conjunto_dados, elemento_pior_caso)
        fim_tempo = time.perf_counter()
        tempo_seq_pior = fim_tempo - inicio_tempo
        
        print(f"{tamanho:<18} | {'Pior Caso':<15} | {'Busca Sequencial':<18} | {tempo_seq_pior:<15.6f} | {visitadas_seq_pior:<20}")

        # Teste: Busca Binária - Pior Caso
        inicio_tempo = time.perf_counter()
        _, visitadas_bin_pior = busca_binaria(conjunto_dados, elemento_pior_caso)
        fim_tempo = time.perf_counter()
        tempo_bin_pior = fim_tempo - inicio_tempo
        
        print(f"{tamanho:<18} | {'Pior Caso':<15} | {'Busca Binária':<18} | {tempo_bin_pior:<15.6f} | {visitadas_bin_pior:<20}")
        
        print("-" * 80)


# --- EXECUÇÃO PRINCIPAL ---
if __name__ == "__main__":
    tamanhos = [1000, 10000, 100000]
    executar_testes(tamanhos)