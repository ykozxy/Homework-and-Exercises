import sys

import Generate_graph


class Vertex:
    def __init__(self, key):
        self.id = key
        self.connected_to = {}

    def add_neighbor(self, nbr, weight=0):
        self.connected_to[nbr] = weight

    def __repr__(self):
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


def deep_search(word_graph, w1, w2):
    line = [word_graph.vert_list[w1]]
    length = 0
    visited = set({})

    def calculate(final):
        nonlocal line, visited, word_graph, length
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
            length += 1
            if calculate(final):
                return True
            else:
                line.pop()
                length -= 1

    calculate(w2)
    return length, [x.id for x in line] + [w2]


def broad_search(word_graph: Graph, w1: str, w2: str):
    visited = set({})
    final = [w2]
    process = [{w1: word_graph.vert_list[w1]}]

    def calculate():
        nonlocal visited, final, process, w1, w2
        # If find
        for each in process[-1].keys():
            if process[-1][each].id == w2:
                return True

        # Create new dict
        process.append({})
        for word in process[-2].keys():
            if process[-2][word].id in visited:
                continue
            visited.add(process[-2][word].id)
            for i in process[-2][word].connected_to.keys():
                if i.id in visited:
                    continue
                process[-1][i.id] = i

        # Recursive sef
        if calculate():
            return True

    # Find path
    calculate()
    last = w2
    for word_set in process[::-1]:
        for word in word_set.keys():
            if last in [x.id for x in word_set[word].connected_to.keys()]:
                last = word
                final.append(last)
                break

    return len(final), final[::-1]


def __main__(word_graph, t='broad'):
    sys.setrecursionlimit(7000)

    w1, w2 = input('First word: '), input('Second word: ')

    print("Calculating......")
    if w1 not in word_graph.vert_list.keys():
        return 'Fail, word 1 not in dict!'
    elif w2 not in word_graph.vert_list.keys():
        return 'Fail, word 2 not in dict!'

    if not word_graph.vert_list[w1].connected_to or not word_graph.vert_list[w2].connected_to:
        return 'No ways! 0 '

    if t == 'deep':
        return deep_search(word_graph, w1, w2)
    elif t == 'broad':
        result = broad_search(word_graph, w1, w2)
        return result if result else "No ways! 1"


if __name__ == '__main__':

    print('Loading...')
    word_graph = Generate_graph.read_data()

    while True:
        print(__main__(word_graph))
