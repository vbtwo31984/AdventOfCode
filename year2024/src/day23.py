from collections import defaultdict
import networkx as nx

class Day23:
    def __init__(self, input):
        self.input = input

    def get_connections(self):
        lines = self.input.splitlines()
        connections = defaultdict(set)
        for line in lines:
            a, b = line.split("-")
            connections[a].add(b)
            connections[b].add(a)
        return connections
    
    def get_triplets(self, connections):
        triplets = set()
        for node in connections:
            for next_node in connections[node]:
                for next_next_node in connections[next_node]:
                    if node in connections[next_next_node]:
                        triplets.add(tuple(sorted((node, next_node, next_next_node))))
        return triplets

    def part1(self):
        connections = self.get_connections()
        triplets = self.get_triplets(connections)
        triplets_starting_with_t = {triplet for triplet in triplets if any(node.startswith("t") for node in triplet)}
        return len(triplets_starting_with_t)
    
    def get_graph(self):
        g = nx.DiGraph().to_undirected()
        lines = self.input.splitlines()
        for line in lines:
            a, b = line.split("-")
            g.add_edge(a, b)
        return g

    def get_longest_cycle(self, graph):
        cycle = sorted(nx.find_cliques(graph), key=len, reverse=True)[0]
        return cycle
            
    def part2(self):
        graph = self.get_graph()
        cycle = self.get_longest_cycle(graph)
        password = ",".join(sorted(cycle))
        return password