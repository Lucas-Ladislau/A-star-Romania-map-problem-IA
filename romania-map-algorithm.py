# Para executar basta abrir o terminal e executar "python3 romania-map-algorithm.py"

class Graph:

    def __init__(self, adjacency_list):
        self.adjacency_list = adjacency_list

    def get_neighbors(self, v):
        return self.adjacency_list[v]

    def h(self, n):
        heuristic = {
            'Arad':          366,
            'Bucharest':     0,
            'Craiova':       160,
            'Dobreta':       242,
            'Eforie':        161,
            'Fagaras':       178,
            'Giurgiu':       77,
            'Hirsova':       151,
            'Iasi':          226,
            'Lugoj':         244,
            'Mehadia':       241,
            'Neamt':         234,
            'Oradea':        380,
            'Pitesti':       98,
            'Rimnicu Vicea': 193,
            'Sibiu':         253,
            'Timisoara':     329,
            'Urziceni':      80,
            'Vaslui':        199,
            'Zerind':        374
        }

        return heuristic[n]

    def a_star_algorithm(self, start_node, stop_node):
        open_list = set([start_node])
        closed_list = set([])
        
        # A variável g contém as distâncias atuais do nó inicial para todos os outros nós.
        g = {}

        g[start_node] = 0

        # O dicionário parents contém um mapa de adjacência de todos os nós
        parents = {}
        parents[start_node] = start_node

        while len(open_list) > 0:
            n = None

            # Verificação de qual nó da lista aberta possui o menor valor
            #f(n) = g(n) + h(n)
            for v in open_list:
                if n == None or g[v] + self.h(v) < g[n] + self.h(n):
                    n = v

            if n == None:
                print('Path does not exist!')
                return None
            
            # verificação se o nó/cidade é o nó/cidade de destino
            if n == stop_node:
                reconst_path = []

                while parents[n] != n:
                    reconst_path.append(n)
                    n = parents[n]

                reconst_path.append(start_node)
                reconst_path.reverse()

                print('Shortest Path: {}'.format(reconst_path))
                return reconst_path

            for (m, weight) in self.get_neighbors(n):
                if m not in open_list and m not in closed_list:
                    open_list.add(m)
                    parents[m] = n
                    g[m] = g[n] + weight
                else:
                    if g[m] > g[n] + weight:
                        g[m] = g[n] + weight
                        parents[m] = n

                        if m in closed_list:
                            closed_list.remove(m)
                            open_list.add(m)

            open_list.remove(n)
            closed_list.add(n)

        print('Path does not exist!')
        return None
    
# Lista de adjacência do Problema mapa da Romênia
adjacency_list = {
    'Arad': [('Zerind', 75), ('Sibiu', 140), ('Timisoara', 118)],
    'Bucharest': [('Pitesti', 101), ('Fagaras', 211), ('Giurgiu', 90), ('Urziceni', 85)],
    'Craiova': [('Pitesti', 138), ('Rimnicu Vicea', 146), ('Dobreta', 120)],
    'Dobreta': [('Craiova', 120), ('Mehadia', 75)],
    'Eforie': [('Hirsova', 86)],
    'Fagaras': [('Sibiu', 99), ('Bucharest', 211)],
    'Giurgiu': [('Bucharest', 90)],
    'Hirsova': [('Eforie', 86), ('Urziceni', 98)],
    'Lugoj': [('Mehadia', 70), ('Timisoara', 111)],
    'Iasi': [('Neamt', 87), ('Vaslui', 92)],
    'Mehadia': [('Lugoj', 70), ('Dobreta', 75)],
    'Neamt': [('Iasi', 87)],
    'Oradea': [('Zerind', 71), ('Sibiu', 151)],
    'Pitesti': [('Bucharest', 101), ('Craiova', 138), ('Rimnicu Vicea', 97)],
    'Rimnicu Vicea': [('Craiova', 146), ('Sibiu', 80), ('Pitesti', 97)],
    'Sibiu': [('Fagaras', 99), ('Rimnicu Vicea', 80), ('Arad', 140), ('Oradea', 151)],
    'Timisoara': [('Arad', 118), ('Lugoj', 111)],
    'Urziceni': [('Bucharest', 85), ('Hirsova', 98), ('Vaslui', 142)],
    'Vaslui': [('Iasi', 92), ('Urziceni', 142)],
    'Zerind': [('Arad', 75), ('Oradea', 71)]
}


mapRomenia = Graph(adjacency_list)
# O problema do mapa da romênia solicita o menor caminho de Arad para Bucarest
#No entanto para se mudar o objetivo final basta adicionar uma nova heuristica
mapRomenia.a_star_algorithm('Arad','Bucharest')