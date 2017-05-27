'''
Question 3

Given an undirected graph G, find the minimum spanning tree within G. A minimum spanning tree connects all vertices in a graph with the smallest possible total weight of edges. Your function should take in and return an adjacency list structured like this:

{'A': [('B', 2)],
 'B': [('A', 2), ('C', 5)],
 'C': [('B', 5)]}

Vertices are represented as unique strings. The function definition should be question3(G)
'''



class Node(object):
    def __init__(self, value):
        self.value = value
        self.edges = []

class Edge(object):
    def __init__(self, value, node_from, node_to):
        self.value = value
        self.node_from = node_from
        self.node_to = node_to

class Graph(object):
    def __init__(self, nodes=[], edges=[]):
        self.nodes = nodes
        self.edges = edges

    def insert_edge(self, new_edge_val, node_from_val, node_to_val):
        from_found = None
        to_found = None
        for node in self.nodes:
            if node_from_val == node.value:
                from_found = node
            if node_to_val == node.value:
                to_found = node
        if from_found == None:
            from_found = Node(node_from_val)
            self.nodes.append(from_found)
        if to_found == None:
            to_found = Node(node_to_val)
            self.nodes.append(to_found)
        new_edge = Edge(new_edge_val, from_found, to_found)
        from_found.edges.append(new_edge)
        to_found.edges.append(new_edge)
        self.edges.append(new_edge)

    def get_edge_list(self):
        """Don't return a list of edge objects!
        Return a list of triples that looks like this:
        (Edge Value, From Node Value, To Node Value)"""
        print len(self.nodes)
        edge_list = []
        for edge_object in self.edges:
            edge = (edge_object.value, edge_object.node_from.value, edge_object.node_to.value)
            edge_list.append(edge)
        return edge_list

    def get_node_list(self):
        """Don't return a list of edge objects!
        Return a list of triples that looks like this:
        (Edge Value, From Node Value, To Node Value)"""
        node_list = []
        for node in self.nodes:
            node = (node.value)
            node_list.append(node)
        return node_list

    def make_set(self, vertex, parent, rank):
        parent[vertex] = vertex
        rank[vertex] = 0

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union(self, parent, rank, v1, v2):
        v1root = self.find(parent, v1)
        v2root = self.find(parent, v2)

        # Attach smaller rank tree under root of high rank tree
        # (Union by Rank)
        if rank[v1root] < rank[v2root]:
            parent[v1root] = v2root
        elif rank[v1root] > rank[v2root]:
            parent[v2root] = v1root
        #If ranks are same, then make one as root and increment
        # its rank by one
        else :
            parent[v1root] = v2root
            rank[v2root] += 1


def ques3(graph):
    # Result
    A = {}

    nodes = graph.get_node_list()
    # len_nodes = len(nodes)

    parent = {}
    rank = {}

    for i, node in enumerate(nodes):
        graph.make_set(node, parent, rank)

    edges = sorted(graph.get_edge_list())

    for w, v1, v2 in edges:
        root1 = graph.find(parent, v1)
        root2 = graph.find(parent, v2)
        if root1 != root2:
            if bool(A.has_key(v1)):
                A[v1].append((w,v2))
                graph.union(root1, root2)
            else:
                A[v1] = (w,v2)
                graph.union(parent, rank, root1, root2)
    return A



graph = Graph()
# graph.insert_edge(10, 0, 1)
# graph.insert_edge(6, 0, 2)
# graph.insert_edge(5, 0, 3)
# graph.insert_edge(15, 1, 3)
# graph.insert_edge(4, 2, 3)

graph.insert_edge(2, 'a', 'b')
graph.insert_edge(3, 'a', 'c')
graph.insert_edge(3, 'a', 'd')
graph.insert_edge(4, 'b', 'c')
graph.insert_edge(3, 'b', 'e')
graph.insert_edge(5, 'c', 'd')
graph.insert_edge(1, 'c', 'e')
graph.insert_edge(7, 'd', 'f')
graph.insert_edge(8, 'e', 'f')
graph.insert_edge(9, 'f', 'g')

print(ques3(graph))
# O(nlogn)


'''
http://www.pythontutor.com/live.html#code=class%20Node%28object%29%3A%0A%20%20%20%20def%20__init__%28self,%20value%29%3A%0A%20%20%20%20%20%20%20%20self.value%20%3D%20value%0A%20%20%20%20%20%20%20%20self.edges%20%3D%20%5B%5D%0A%0Aclass%20Edge%28object%29%3A%0A%20%20%20%20def%20__init__%28self,%20value,%20node_from,%20node_to%29%3A%0A%20%20%20%20%20%20%20%20self.value%20%3D%20value%0A%20%20%20%20%20%20%20%20self.node_from%20%3D%20node_from%0A%20%20%20%20%20%20%20%20self.node_to%20%3D%20node_to%0A%0Aclass%20Graph%28object%29%3A%0A%20%20%20%20def%20__init__%28self,%20nodes%3D%5B%5D,%20edges%3D%5B%5D%29%3A%0A%20%20%20%20%20%20%20%20self.nodes%20%3D%20nodes%0A%20%20%20%20%20%20%20%20self.edges%20%3D%20edges%0A%0A%20%20%20%20def%20insert_edge%28self,%20new_edge_val,%20node_from_val,%20node_to_val%29%3A%0A%20%20%20%20%20%20%20%20from_found%20%3D%20None%0A%20%20%20%20%20%20%20%20to_found%20%3D%20None%0A%20%20%20%20%20%20%20%20for%20node%20in%20self.nodes%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20if%20node_from_val%20%3D%3D%20node.value%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20from_found%20%3D%20node%0A%20%20%20%20%20%20%20%20%20%20%20%20if%20node_to_val%20%3D%3D%20node.value%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20to_found%20%3D%20node%0A%20%20%20%20%20%20%20%20if%20from_found%20%3D%3D%20None%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20from_found%20%3D%20Node%28node_from_val%29%0A%20%20%20%20%20%20%20%20%20%20%20%20self.nodes.append%28from_found%29%0A%20%20%20%20%20%20%20%20if%20to_found%20%3D%3D%20None%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20to_found%20%3D%20Node%28node_to_val%29%0A%20%20%20%20%20%20%20%20%20%20%20%20self.nodes.append%28to_found%29%0A%20%20%20%20%20%20%20%20new_edge%20%3D%20Edge%28new_edge_val,%20from_found,%20to_found%29%0A%20%20%20%20%20%20%20%20from_found.edges.append%28new_edge%29%0A%20%20%20%20%20%20%20%20to_found.edges.append%28new_edge%29%0A%20%20%20%20%20%20%20%20self.edges.append%28new_edge%29%0A%0A%20%20%20%20def%20get_edge_list%28self%29%3A%0A%20%20%20%20%20%20%20%20%22%22%22Don't%20return%20a%20list%20of%20edge%20objects!%0A%20%20%20%20%20%20%20%20Return%20a%20list%20of%20triples%20that%20looks%20like%20this%3A%0A%20%20%20%20%20%20%20%20%28Edge%20Value,%20From%20Node%20Value,%20To%20Node%20Value%29%22%22%22%0A%20%20%20%20%20%20%20%20print%20len%28self.nodes%29%0A%20%20%20%20%20%20%20%20edge_list%20%3D%20%5B%5D%0A%20%20%20%20%20%20%20%20for%20edge_object%20in%20self.edges%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20edge%20%3D%20%28edge_object.value,%20edge_object.node_from.value,%20edge_object.node_to.value%29%0A%20%20%20%20%20%20%20%20%20%20%20%20edge_list.append%28edge%29%0A%20%20%20%20%20%20%20%20return%20edge_list%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20def%20get_node_list%28self%29%3A%0A%20%20%20%20%20%20%20%20%22%22%22Don't%20return%20a%20list%20of%20edge%20objects!%0A%20%20%20%20%20%20%20%20Return%20a%20list%20of%20triples%20that%20looks%20like%20this%3A%0A%20%20%20%20%20%20%20%20%28Edge%20Value,%20From%20Node%20Value,%20To%20Node%20Value%29%22%22%22%0A%20%20%20%20%20%20%20%20node_list%20%3D%20%5B%5D%0A%20%20%20%20%20%20%20%20for%20node%20in%20self.nodes%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20node%20%3D%20%28node.value%29%0A%20%20%20%20%20%20%20%20%20%20%20%20node_list.append%28node%29%0A%20%20%20%20%20%20%20%20return%20node_list%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20def%20make_set%28self,%20vertex,%20parent,%20rank%29%3A%0A%20%20%20%20%20%20%20%20parent%5Bvertex%5D%20%3D%20vertex%0A%20%20%20%20%20%20%20%20rank%5Bvertex%5D%20%3D%200%0A%0A%0Adef%20ques3%28graph%29%3A%0A%20%20%20%20A%20%3D%20%5B%5D%0A%0A%20%20%20%20nodes%20%3D%20graph.get_node_list%28%29%0A%20%20%20%20len_nodes%20%3D%20len%28nodes%29%0A%0A%20%20%20%20parent%20%3D%20%7B%7D%0A%20%20%20%20rank%20%3D%20%7B%7D%0A%0A%20%20%20%20for%20i,%20node%20in%20enumerate%28nodes%29%3A%0A%20%20%20%20%20%20%20%20%23%20parent.append%28node%29%0A%20%20%20%20%20%20%20%20%23%20rank.append%280%29%0A%20%20%20%20%20%20%20%20graph.make_set%28node,%20parent,%20rank%29%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20print%20parent%0A%20%20%20%20%20%20%20%20%0A%0A%0A%0Agraph%20%3D%20Graph%28%29%0Agraph.insert_edge%282,%20'a',%20'b'%29%0Agraph.insert_edge%283,%20'a',%20'c'%29%0Agraph.insert_edge%283,%20'a',%20'd'%29%0Agraph.insert_edge%284,%20'b',%20'c'%29%0Agraph.insert_edge%283,%20'b',%20'e'%29%0Agraph.insert_edge%285,%20'c',%20'd'%29%0Agraph.insert_edge%281,%20'c',%20'e'%29%0Agraph.insert_edge%287,%20'd',%20'f'%29%0Agraph.insert_edge%288,%20'e',%20'f'%29%0Agraph.insert_edge%289,%20'f',%20'g'%29%0A%0Aprint%28ques3%28graph%29%29%0A&cumulative=false&curInstr=432&heapPrimitives=false&mode=display&origin=opt-live.js&py=2&rawInputLstJSON=%5B%5D&textReferences=false

'''
