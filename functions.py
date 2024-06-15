# Importando bibliotecas necessárias
import networkx as nx
import matplotlib.pyplot as plt
import random

def generate_matrix_graph(n, m):
    """
    Plota um grafo em forma de matriz de dimensão n x m.
 
    Args:
    n (int): Número de linhas.
    m (int): Número de colunas.
    """
    # Cria o grafo de grade
    G = nx.grid_2d_graph(n, m)
    # Mapeia os nós para coordenadas 2D
    pos = {(x, y): (y, -x) for x, y in G.nodes()}
    # Desenha o grafo
    plt.figure(figsize=(8, 8))
    nx.draw(G, pos=pos, with_labels=True, node_size=20, node_color="skyblue", font_weight="bold")
    plt.title(f"Grafo de Grade {n}x{m}")
    plt.show()
 
    return G

def generate_graph_from_path(num_vertices):
    """
    Gera um grafo a partir de um caminho linear de vértices.

    Args:
    num_vertices (int): Número de vértices no caminho.

    Returns:
    G (networkx.Graph): Grafo gerado.
    path_vertices (list): Lista de vértices no caminho.
    """
    # Define os vértices do caminho de A até B
    path_vertices = ['A'] + [str(i) for i in range(1, num_vertices-1)] + ['B']
    
    # Cria um dicionário para representar o grafo
    path_dict = {}
    for i in range(len(path_vertices)-1):
        if path_vertices[i] not in path_dict:
            path_dict[path_vertices[i]] = {}
        path_dict[path_vertices[i]][path_vertices[i+1]] = random.randint(1, 10)
    
    # Adiciona arestas aleatórias para os vértices restantes
    for i in range(1, num_vertices-1):
        neighbors = random.sample(path_vertices[:i] + path_vertices[i+1:], random.randint(1, num_vertices-2))
        if path_vertices[i] not in path_dict:
            path_dict[path_vertices[i]] = {}
        for neighbor in neighbors:
            if neighbor not in path_dict[path_vertices[i]]:
                path_dict[path_vertices[i]][neighbor] = random.randint(1, 10)
            if neighbor not in path_dict:
                path_dict[neighbor] = {}
            path_dict[neighbor][path_vertices[i]] = path_dict[path_vertices[i]][neighbor]  # Aresta bidirecional
    
    G = nx.Graph()
    
    # Adiciona os vértices e arestas ao grafo
    for node, edges in path_dict.items():
        for neighbor, distance in edges.items():
            G.add_edge(node, neighbor, weight=distance)
    
    return G, path_vertices

def plot_graph(G):
    """
    Plota um grafo utilizando layout 'spring'.

    Args:
    G (networkx.Graph): Grafo a ser plotado.
    """
    pos = nx.spring_layout(G)  # Layout usando o algoritmo 'spring'
    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=500, edge_color='black', linewidths=1, font_size=15)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.show()

def calculate_path_distance(G, path):
    """
    Calcula a distância total de um caminho em um grafo.

    Args:
    G (networkx.Graph): Grafo contendo os caminhos.
    path (list): Lista de vértices representando o caminho.

    Returns:
    total_distance (int): Distância total do caminho ou None se o caminho for inválido.
    """
    total_distance = 0
    for i in range(len(path) - 1):
        try:
            total_distance += G[path[i]][path[i+1]]['weight']  # Soma todos os valores das arestas
        except KeyError:
            return None
    return total_distance

def show_neighbors(G, vertex):
    """
    Retorna os vizinhos de um vértice em um grafo.

    Args:
    G (networkx.Graph): Grafo contendo os vértices.
    vertex: Vértice cujo vizinhos serão retornados.

    Returns:
    neighbors (list): Lista de vizinhos do vértice.
    """
    neighbors = list(G.neighbors(vertex))  # Lista de vizinhos
    return neighbors

def gerar_caminho(G, start_vertex, end_vertex):
    """
    Gera um caminho aleatório de start_vertex até end_vertex.

    Args:
    G (networkx.Graph): Grafo contendo os vértices.
    start_vertex: Vértice de início.
    end_vertex: Vértice de destino.

    Returns:
    caminho (list): Lista de vértices representando o caminho.
    """
    caminho = [start_vertex]
    current_vertex = start_vertex
        
    while current_vertex != end_vertex:
        vizinhos = show_neighbors(G, current_vertex)
        if not vizinhos:
            break  # Se não houver vizinhos, terminar o caminho
        
        # Se end_vertex é vizinho do current_vertex, selecioná-lo
        if end_vertex in vizinhos:
            caminho.append(end_vertex)
            break
        
        next_vertex = random.choice(vizinhos)
            
        # Evitar ciclos removendo o vértice anterior dos vizinhos
        if len(caminho) > 1 and next_vertex == caminho[-2]:
            vizinhos.remove(next_vertex)
            if not vizinhos:
                break
            next_vertex = random.choice(vizinhos)
            
        caminho.append(next_vertex)
        current_vertex = next_vertex
    
    return caminho

def populacao_de_caminhos(G, start_vertex, end_vertex, n):
    """
    Gera uma população de caminhos de start_vertex até end_vertex.

    Args:
    G (networkx.Graph): Grafo contendo os vértices.
    start_vertex: Vértice de início.
    end_vertex: Vértice de destino.
    n (int): Número de caminhos a serem gerados.

    Returns:
    populacao (list): Lista de caminhos.
    """
    populacao = []
    
    for _ in range(n):
        #Gerando n caminhos aleatórios
        caminho = gerar_caminho(G, start_vertex, end_vertex) 
        if caminho[-1] == end_vertex:
            populacao.append(caminho)
    return populacao

def funcao_objetivo_grafo(populacao, G):
    """
    Computa a função objetivo de uma população de caminhos de grafos.

    Args:
    populacao (list): Lista contendo os indivíduos do problema.
    G (networkx.Graph): Grafo contendo os caminhos.

    Returns:
    fitness (list): Lista de valores de aptidão (distância total) para cada caminho.
    """
    fitness = []

    for individuo in populacao:
        #Coleta a distãncia total do caminho do indivíduo
        fitness.append(calculate_path_distance(G, individuo))

    return fitness

def selecao_torneio_min(populacao, fitness, tamanho_torneio):
    """
    Faz a seleção de uma população usando torneio.

    Nota: da forma que está implementada, só funciona em problemas de minimização.

    Args:
    populacao (list): Lista contendo os indivíduos do problema.
    fitness (list): Lista contendo os valores computados da função objetivo.
    tamanho_torneio (int): Quantidade de indivíduos que batalham entre si.

    Returns:
    selecionados (list): Lista de indivíduos selecionados.
    """
    selecionados = []

    for _ in range(len(populacao)):
        sorteados = random.sample(populacao, tamanho_torneio)

        fitness_sorteados = []
        for individuo in sorteados:
            indice_individuo = populacao.index(individuo)
            fitness_sorteados.append(fitness[indice_individuo])

        min_fitness = min(fitness_sorteados)
        indice_min_fitness = fitness_sorteados.index(min_fitness)
        individuo_selecionado = sorteados[indice_min_fitness]

        selecionados.append(individuo_selecionado)

    return selecionados

def mutacao_troca(G, populacao, chance_de_mutacao, end_vertex):
    """
    Aplica mutação de troca em um indivíduo.

    Args:
    G (networkx.Graph): Grafo contendo os vértices.
    populacao (list): Lista contendo os indivíduos do problema.
    chance_de_mutacao (float): Chance de mutação (entre 0 e 1).
    end_vertex: Vértice de destino.
    """
    for individuo in populacao:
        if random.random() < chance_de_mutacao:
            # Seleciona um gene aleatório para mutação (exceto o início e o fim)
            gene = random.randint(1, len(individuo) - 2)
            start_vertex = individuo[gene]
            
            # Gera um novo caminho a partir do ponto de mutação até o final
            novo_caminho = gerar_caminho(G, start_vertex, end_vertex)
            individuo = individuo[:gene-1] + novo_caminho
            

def cruzamento_cruzado(pai, mae, chance_de_cruzamento):
    """
    Gera um cruzamento entre dois indivíduos inspirado em um corte duplo, mas situacional.

    Args:
    pai (list): indivíduo pai.
    mae (list): indivíduo mãe.
    chance_de_cruzamento (float): chance de ocorrer o cruzamento (0 a 1).

    Returns:
    tuple: Dois indivíduos resultantes do cruzamento ou os indivíduos originais.
    """
    if random.random() < chance_de_cruzamento:
        # Excluir índices iniciais, finais, segundo e penúltimo
        pai_validos = pai[2:-2]
        mae_validos = mae[2:-2]
        
        # Encontrar interseção dos vértices válidos
        pontos_comuns = set(pai_validos).intersection(mae_validos)
        
        if pontos_comuns:
            ponto_de_corte = random.choice(list(pontos_comuns))
            
            # Encontrar os índices reais no pai e na mãe
            indice_pai = pai.index(ponto_de_corte)
            indice_mae = mae.index(ponto_de_corte)
            
            # Realizar o cruzamento
            filho1 = pai[:indice_pai] + mae[indice_mae:]
            filho2 = mae[:indice_mae] + pai[indice_pai:]
            
            return filho1, filho2
        
    return pai, mae
            
