import time
import random
import matplotlib.pyplot as plt
import numpy as np

# --- ALGORITMOS DE BUSCA ---

def busca_sequencial(lista, elemento):
    posicoes_visitadas = 0
    for i, item in enumerate(lista):
        posicoes_visitadas += 1
        if item == elemento:
            return i, posicoes_visitadas
    return -1, posicoes_visitadas

def busca_binaria(lista, elemento):
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

# --- FUNÇÃO DE TESTES ---

def executar_testes(tamanhos_entrada):
    resultados_completos = []
    print("Comparação de desempenho: Busca Sequencial vs. Busca Binária")
    print("-" * 80)
    print(f"{'Tamanho Entrada':<18} | {'Tipo de Caso':<15} | {'Algoritmo':<18} | {'Tempo (s)':<15} | {'Posições Visitadas':<20}")
    print("-" * 80)

    for tamanho in tamanhos_entrada:
        conjunto_dados = sorted(random.sample(range(tamanho * 2), tamanho))
        
        # --- CASO MÉDIO ---
        elemento_medio = random.choice(conjunto_dados)

        # Teste Sequencial - Médio
        inicio_tempo = time.perf_counter()
        _, visitadas_seq_medio = busca_sequencial(conjunto_dados, elemento_medio)
        tempo_seq_medio = time.perf_counter() - inicio_tempo
        print(f"{tamanho:<18} | {'Caso Médio':<15} | {'Busca Sequencial':<18} | {tempo_seq_medio:<15.6f} | {visitadas_seq_medio:<20}")
        resultados_completos.append({'tamanho': tamanho, 'caso': 'Médio', 'algoritmo': 'Sequencial', 'tempo': tempo_seq_medio, 'visitas': visitadas_seq_medio})
        
        # Teste Binária - Médio
        inicio_tempo = time.perf_counter()
        _, visitadas_bin_medio = busca_binaria(conjunto_dados, elemento_medio)
        tempo_bin_medio = time.perf_counter() - inicio_tempo
        print(f"{tamanho:<18} | {'Caso Médio':<15} | {'Busca Binária':<18} | {tempo_bin_medio:<15.6f} | {visitadas_bin_medio:<20}")
        resultados_completos.append({'tamanho': tamanho, 'caso': 'Médio', 'algoritmo': 'Binária', 'tempo': tempo_bin_medio, 'visitas': visitadas_bin_medio})

        # --- PIOR CASO ---
        elemento_pior_caso = tamanho * 2 + 1 

        # Teste Sequencial - Pior
        inicio_tempo = time.perf_counter()
        _, visitadas_seq_pior = busca_sequencial(conjunto_dados, elemento_pior_caso)
        tempo_seq_pior = time.perf_counter() - inicio_tempo
        print(f"{tamanho:<18} | {'Pior Caso':<15} | {'Busca Sequencial':<18} | {tempo_seq_pior:<15.6f} | {visitadas_seq_pior:<20}")
        resultados_completos.append({'tamanho': tamanho, 'caso': 'Pior', 'algoritmo': 'Sequencial', 'tempo': tempo_seq_pior, 'visitas': visitadas_seq_pior})
        
        # Teste Binária - Pior
        inicio_tempo = time.perf_counter()
        _, visitadas_bin_pior = busca_binaria(conjunto_dados, elemento_pior_caso)
        tempo_bin_pior = time.perf_counter() - inicio_tempo
        print(f"{tamanho:<18} | {'Pior Caso':<15} | {'Busca Binária':<18} | {tempo_bin_pior:<15.6f} | {visitadas_bin_pior:<20}")
        resultados_completos.append({'tamanho': tamanho, 'caso': 'Pior', 'algoritmo': 'Binária', 'tempo': tempo_bin_pior, 'visitas': visitadas_bin_pior})
        
        print("-" * 80)
    
    return resultados_completos

# --- GRÁFICOS COM CURVAS TEÓRICAS E TICKS FIXOS ---

def gerar_graficos(resultados, tamanhos):
    tempos_seq = [r['tempo'] for r in resultados if r['algoritmo'] == 'Sequencial' and r['caso'] == 'Pior']
    visitas_seq = [r['visitas'] for r in resultados if r['algoritmo'] == 'Sequencial' and r['caso'] == 'Pior']
    tempos_bin = [r['tempo'] for r in resultados if r['algoritmo'] == 'Binária' and r['caso'] == 'Pior']
    visitas_bin = [r['visitas'] for r in resultados if r['algoritmo'] == 'Binária' and r['caso'] == 'Pior']

    plt.style.use("seaborn-v0_8-colorblind")

    fig, axs = plt.subplots(1, 2, figsize=(16, 6))

    tamanhos_np = np.array(tamanhos)
    on_curve = tamanhos_np / max(tamanhos_np) * max(tempos_seq)
    logn_curve = np.log2(tamanhos_np) / np.log2(max(tamanhos_np)) * max(tempos_bin)

    # Tempo
    axs[0].plot(tamanhos, tempos_seq, '-o', label='Busca Sequencial', color='crimson')
    axs[0].plot(tamanhos, tempos_bin, '-s', label='Busca Binária', color='seagreen')
    axs[0].plot(tamanhos, on_curve, '--', label='Referência O(n)', color='crimson', alpha=0.5)
    axs[0].plot(tamanhos, logn_curve, '--', label='Referência O(log n)', color='seagreen', alpha=0.5)
    axs[0].set_title('Tempo de Execução (Pior Caso)', fontsize=14)
    axs[0].set_xlabel('Tamanho da Entrada (n)', fontsize=12)
    axs[0].set_ylabel('Tempo (s)', fontsize=12)
    axs[0].set_xticks(tamanhos)  # <- TICKS FIXOS
    axs[0].legend(fontsize=10)
    axs[0].grid(True)

    # Posições visitadas
    axs[1].plot(tamanhos, visitas_seq, '-o', label='Busca Sequencial', color='crimson')
    axs[1].plot(tamanhos, visitas_bin, '-s', label='Busca Binária', color='seagreen')
    axs[1].plot(tamanhos, tamanhos_np, '--', label='Referência O(n)', color='crimson', alpha=0.5)
    axs[1].plot(tamanhos, np.log2(tamanhos_np), '--', label='Referência O(log n)', color='seagreen', alpha=0.5)
    axs[1].set_title('Posições Visitadas (Pior Caso)', fontsize=14)
    axs[1].set_xlabel('Tamanho da Entrada (n)', fontsize=12)
    axs[1].set_ylabel('Posições Visitadas (escala log)', fontsize=12)
    axs[1].set_xticks(tamanhos)  # <- TICKS FIXOS
    axs[1].set_yscale('log')
    axs[1].legend(fontsize=10)
    axs[1].grid(True, which="both", ls="-")

    fig.suptitle('Análise Comparativa de Desempenho: Busca Sequencial vs. Binária (Pior Caso)', fontsize=16)
    fig.tight_layout(rect=[0, 0.03, 1, 0.95])

    plt.savefig('graficos_comparativos.png', dpi=300)
    plt.savefig('graficos_comparativos.svg')
    print("\nGráficos salvos com sucesso em 'graficos_comparativos.png' e '.svg'")
    plt.show()

# --- EXECUÇÃO ---

if __name__ == "__main__":
    tamanhos_de_entrada = [1000, 10000, 100000]
    dados_coletados = executar_testes(tamanhos_de_entrada)
    gerar_graficos(dados_coletados, tamanhos_de_entrada)
