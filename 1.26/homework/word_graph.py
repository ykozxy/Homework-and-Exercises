import os
import pickle
import sys

import Generate_graph


class Vertex:
    def __init__(self, key):
        self.id = key
        self.connected_to = {}

    def add_neighbor(self, nbr, weight=0):
        self.connected_to[nbr] = weight

    def __str__(self):
        return str(self.id) + ' connected to: ' + str([x.id for x in self.connected_to])

    def get_connections(self):
        return self.connected_to.keys()

    def get_id(self):
        return self.id

    def get_weight(self, nbr):
        return self.connected_to[nbr]


class Graph:
    def __init__(self):
        self.vert_list = {}
        self.num_vertices = 0

    def add_vertex(self, key):
        self.num_vertices += 1
        self.vert_list[key] = Vertex(key)

    def get_vertex(self, n):
        if n in self.vert_list.keys():
            return self.vert_list[n]
        return None

    def add_edge(self, f, t, cost=0):
        if f not in self.vert_list:
            self.add_vertex(f)
        if t not in self.vert_list:
            self.add_vertex(t)
        self.vert_list[f].add_neighbor(self.vert_list[t], weight=cost)

    def get_vertices(self):
        return self.vert_list.keys()

    def __iter__(self):
        return iter(self.vert_list.values())


def __main__():
    sys.setrecursionlimit(7000)

    if 'WordGraph.graph' not in os.listdir(os.getcwd()):
        Generate_graph.__main__()
    with open('WordGraph.graph', 'rb') as f:
        word_graph: Graph = pickle.load(f)

    # w1, w2 = input('First word: '), input('Second word: ')
    w1, w2 = 'bill', 'biff'

    print("Calculating......")
    if w1 not in word_graph.vert_list.keys():
        return 'Fail, word 1 not in dict!'
    elif w2 not in word_graph.vert_list.keys():
        return 'Fail, word 2 not in dict!'

    if not word_graph.vert_list[w1].connected_to or not word_graph.vert_list[w2].connected_to:
        return 'No ways! 0 '

    line = [word_graph.vert_list[w1]]
    visited = set({})

    def calculate(final):
        nonlocal line, visited, word_graph
        # Is found
        for each in line[-1].connected_to:
            if final == each.id:
                return True

        # Others
        for each in line[-1].connected_to:
            if each in visited:
                continue
            visited.add(each)
            line.append(each)
            if calculate(final) is True:
                return True
            else:
                line.pop()

    calculate(w2)
    return [x.id for x in line] + [w2]


if __name__ == '__main__':
    print(__main__())
