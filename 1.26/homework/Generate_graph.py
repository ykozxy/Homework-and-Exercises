import sys


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


def is_vicinity(word1, word2):
    count = 1
    for i in range(4):
        if word1[i] != word2[i]:
            count -= 1
    return count >= 0


def add_word(word_graph: Graph, word: str):
    if word in word_graph.vert_list.keys():
        return
    word_graph.add_vertex(word)
    for each in word_graph.vert_list.keys():
        if is_vicinity(word, each):
            word_graph.add_edge(word, each)
            word_graph.add_edge(each, word)
    return


def save_data(word_graph: Graph):
    with open('WordGraph', 'w') as f:
        # Save all words
        for i in word_graph.vert_list.values():
            f.write(f'{i.id} ')
        # Save Graph
        for word in word_graph.vert_list.values():
            f.write(f"{word.id} ")
            for connect in word.connected_to.keys():
                f.write(f'{connect.id} ')
            f.write('\n')


def read_data() -> Graph:
    word_graph = Graph()
    with open('WordGraph', 'r') as f:
        # Add Vertex
        total_word = f.readline().split()
        for word in total_word:
            word_graph.add_vertex(word)

        # Add Edges
        line = f.readline()
        while line:
            words = line.split()
            for i in words[1:]:
                word_graph.add_edge(words[0], i)
                word_graph.add_edge(i, words[0])
            line = f.readline()
    return word_graph


def __main__(save=True):
    sys.setrecursionlimit(15000)

    total_words = []
    print('Generating word list...')
    with open('4-letter.txt', 'r') as words:
        while True:
            temp = words.readline()
            if not temp:
                break
            total_words.append(temp[: 4])

    print("Start to generate Graph")
    word_graph = Graph()

    print('Adding vertex...')
    for each in total_words:
        word_graph.add_vertex(each)

    print('Generating graph...')
    count = 0
    for pos_w1, w1 in enumerate(total_words):
        process = str(((pos_w1 + 1) / 5304) * 100)[: 4]
        if count == 50:
            print(process + '%%   %s' % w1)
        count += 1 if count < 50 else -50
        for w2 in total_words[pos_w1 + 1:]:
            if is_vicinity(w1, w2):
                word_graph.add_edge(w1, w2)
                word_graph.add_edge(w2, w1)

    if save:
        print('Saving data......')
        save_data(word_graph)
        print('Data saved!')
    return word_graph


if __name__ == '__main__':
    data = read_data()
    pass
