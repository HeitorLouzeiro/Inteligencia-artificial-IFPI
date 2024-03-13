import sys

import matplotlib.pyplot as plt
import networkx as nx


class DijkstraAlgorithm:
    def __init__(self, vertices, city_names):
        self.V = vertices
        self.graph = [[0 for _ in range(vertices)] for _ in range(vertices)]
        self.city_names = city_names

    def minimum_distance(self, distances, visited):
        min_distance = sys.maxsize
        min_index = -1

        for v in range(self.V):
            if not visited[v] and distances[v] <= min_distance:
                min_distance = distances[v]
                min_index = v

        return min_index

    def print_path(self, distances, parent, source, destination):
        print(
            f"Caminho mínimo entre {self.city_names[source]} e {self.city_names[destination]}: ", end='')
        crawl = destination
        print(self.city_names[crawl], end='')

        while parent[crawl] != -1:
            print(f" <- {self.city_names[parent[crawl]]}", end='')
            crawl = parent[crawl]

        print(f"\nKm total: {distances[destination]} Km")

    def dijkstra(self, source, destination):
        distances = [sys.maxsize] * self.V
        visited = [False] * self.V
        parent = [-1] * self.V
        distances[source] = 0

        for _ in range(self.V - 1):
            u = self.minimum_distance(distances, visited)
            visited[u] = True

            for v in range(self.V):
                if not visited[v] and self.graph[u][v] != 0 and distances[u] != sys.maxsize and distances[u] + self.graph[u][v] < distances[v]:
                    distances[v] = distances[u] + self.graph[u][v]
                    parent[v] = u

        self.print_path(distances, parent, source, destination)
        self.visualize_graph()

    def visualize_graph(self):
        G = nx.Graph()

        for i, city in enumerate(self.city_names):
            G.add_node(city)

        for i in range(self.V):
            for j in range(i + 1, self.V):
                weight = self.graph[i][j]
                if weight != 0:
                    G.add_edge(self.city_names[i],
                               self.city_names[j], weight=weight)

        pos = nx.spring_layout(G)
        labels = nx.get_edge_attributes(G, 'weight')
        nx.draw(G, pos, with_labels=True, font_weight='bold')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
        plt.show()


# Programa principal para testar o algoritmo
if __name__ == "__main__":
    city_names = ["Corrente", "Barreiras", "Correntina",
                  "Roda Velha", "Alvorada Norte", "Brasília"]
    vertices = len(city_names)
    graph = [
        [0, 230, 0, 0, 0, 0],
        [230, 0, 138, 166, 0, 0],
        [0, 138, 0, 0, 224, 0],
        [0, 166, 0, 0, 273, 0],
        [0, 0, 224, 273, 0, 255],
        [0, 0, 0, 0, 255, 0]
    ]
    source = 0
    destination = 5

    dijkstra = DijkstraAlgorithm(vertices, city_names)
    dijkstra.graph = graph
    dijkstra.dijkstra(source, destination)
