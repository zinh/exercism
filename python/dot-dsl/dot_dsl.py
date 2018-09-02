NODE, EDGE, ATTR = range(3)


class Node(object):
    def __init__(self, name, attrs={}):
        self.name = name
        self.attrs = attrs

    def __eq__(self, other):
        return self.name == other.name and self.attrs == other.attrs


class Edge(object):
    def __init__(self, src, dst, attrs={}):
        self.src = src
        self.dst = dst
        self.attrs = attrs

    def __eq__(self, other):
        return (self.src == other.src and
                self.dst == other.dst and
                self.attrs == other.attrs)


class Graph(object):
    def __init__(self, data=[]):
        self.nodes, self.edges, self.attrs = [], [], {}
        for child in data:
            if len(child) <= 1:
                raise TypeError("Invalid item")
            if child[0] == NODE:
                if not isinstance(child[2], dict):
                    raise ValueError("Invalid node")
                self.nodes.append(Node(child[1], child[2]))
            elif child[0] == EDGE:
                if len(child) < 4:
                    raise ValueError("Invalid edge")
                self.edges.append(Edge(child[1], child[2], child[3]))
            elif child[0] == ATTR:
                if len(child) != 3:
                    raise ValueError("Invalid attr")
                self.attrs[child[1]] = child[2]
            else:
                raise ValueError("Unknow item")
