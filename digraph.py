"""
Simple Python implementation of a directed graph.
"""


class Digraph:

    def __init__(self):
        """
        Initialize a digraph.
        """
        self.node_neighbors = {}  # Pairing: Node -> Neighbors
        self.node_incidence = {}  # Pairing: Node -> Incident nodes

    def nodes(self):
        """
        Return node list.

        @rtype:  list
        @return: Node list.
        """
        return list(self.node_neighbors.keys())

    def neighbors(self, node):
        """
        Return all nodes that are directly accessible from given node.

        @rtype:  list
        @return: List of nodes directly accessible from given node.
        """
        return self.node_neighbors[node]

    def incidents(self, node):
        """
        Return all nodes that are incident to the given node.

        @rtype:  list
        @return: List of nodes directly accessible from given node.
        """
        return self.node_incidence[node]

    def add_node(self, node):
        """
        Add given node to the graph.

        @type  node: node
        @param node: Node identifier.
        """
        if node not in self.node_neighbors:
            self.node_neighbors[node] = []
            self.node_incidence[node] = []
        else:
            print("Node %s already in digraph" % node)

    def add_nodes(self, nodelist):
        """
        Add given nodes to the graph.

        @type  nodelist: list
        @param nodelist: List of nodes to be added to the graph.
        """
        for each in nodelist:
            self.add_node(each)

    def add_edge(self, edge):
        """
        Add a directed edge to the graph connecting two nodes.

        An edge, here, is a pair of nodes like C{(n, m)}.

        @type  edge: tuple
        @param edge: Edge.
        """
        u, v = edge
        for n in [u, v]:
            if not n in self.node_neighbors:
                print("%s is missing from the node_neighbors table" % n)
            if not n in self.node_incidence:
                print("%s is missing from the node_incidence table" % n)

        if v in self.node_neighbors[u] and u in self.node_incidence[v]:
            print("Edge (%s, %s) already in digraph" % (u, v))
        else:
            self.node_neighbors[u].append(v)
            self.node_incidence[v].append(u)
