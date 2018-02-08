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
        self.vert_list[t].add_neighbor(self.vert_list[f], weight=cost)

    def get_vertices(self):
        return self.vert_list.keys()

    def __iter__(self):
        return iter(self.vert_list.values())


g = Graph()
for i in range(4):
    g.add_vertex(i)
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(0, 2)
g.add_edge(3, 2)

for v in g:
    for w in v.get_connections():
        print("(%s, %s)" % (v.get_id(), w.get_id()))
