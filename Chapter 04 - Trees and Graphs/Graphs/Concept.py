"""
    GRAPHS
    A tree is actually a type of graph, but not all graphs are trees. Simply put, a tree is a connected graph without
cycles.
    A graph is simply a collection of nodes with edges between (some of) them.
        *   Graphs can be directed or undirected - While edges are like a one-way street, undirected edges are like
            a two-way street.
        *   The graph might consist of multiple isolated sub-graphs. If there is a path between every pair of vertices,
            it is called a "connected graph"
        *   The graph can also have cycles (or not). An "acyclic graph" is one without cycles.
"""

"""
    ADJACENCY LIST
    This is the most common way to represent a graph. Every vertex (or node) stores a list of adjacent vertices.
    In an undirected graph, an edge like (a, b) would be stored twice: 
        1. Once in a's adjacent vertices
        2. Once in b's adjacent vertices
"""


# A simple class definition for a graph node could look essentially the same as a tree node
class Graph:

    def __init__(self):
        self.Nodes = []


class Node:

    def __init__(self):
        self.name = None  # String type
        self.children = []


"""
    The Graph class is used because, unlike in a tree, you can't necessarily reach all the nodes from a single node.
    You don't necessarily need any additional classes to represent a graph. An array (or a hash table) of lists.
(arrays, arraylists, linked lists, etc) can store the adjacency list. The graph above could be represented as:

    * See book, page 106 *
    0: 1
    1: 2
    2: 0, 3
    3: 2
    4: 6
    5: 4
    6: 5
    
    This is a bit more compact, but it is not quite as clean. We tend to use node classes unless there's a 
compelling reason not to.

    
    ADJACENCY MATRICES
    An adjacency matrix is an NxN boolean matrix (where N is the number of nodes), where a true value at matrix[i][j]
indicates an edge from node i to node j. (You can also use an integer matrix with 0x and 1s)
    In an undirected graph, an adjacency matrix will be symmetric.
    In an directed graph, it will not (necessarily) 
"""

"""
    GRAPH SEARCH
    The two most common ways to search a graph are depth-first search (DFS) and breadth-first-search (BFS).
    
    DFS
    We start at the root (or another arbitrarily selected node) and explore each branch completely before moving on 
to the next branch. That is, we go deep first (before we go wide)

    BFS
    We start at the root (or another arbitrarily selected node) and explore each neighbor before going on 
to any of their children. That is, we go wide first before we go deep.

    BFS and DFS tend to be used in different scenarios. DFS is often preferred if we want to visit every node in 
the graph. Both will work just fine, but depth-first search is a bit simpler.
    However, if we want to find the shortest path (or just any path) between two nodes, BFS is generally better. 

"""

"""
    DEPTH-FIRST-SEARCH IMPLEMENTATION

    In DPS we first visit a node A and then iterate through each of A's neighbors. 
    When visiting a node B that is a neighbor of A, we visit all of B's neighbors before going on to A's 
other neighbors. 
    That is, a exhaustively searches B's breanch before any of its other neighbors. 

    NOTE: pre-order and other forms of tree traversal are a form of DFS. The key difference is that when 
implementing this algorithm for a graph, we musch check if the node has been visited. If we don't, we risk getting 
stuck in an infinite loop.
"""


def visit(node):
    pass


def dps_search(root):
    if root is None:
        return

    visit(root)  # Do necessary actions
    root.visited = True

    for node in root.adjacent:
        if node.visited is False:
            dps_search(node)


"""
    BREATH-FIRST-SEARCH IMPLEMENTATION
    BFS is a bit less intuitive, and many interviewees struggle with the implementation unless they are 
already familiar with it. THE MAIN tripping point is the (false) assumption that BFS is recursive. It is not. Instead, 
it uses a queue.
    In BFS, node a visits each of A's neighbors before visiting any of their neighbors. You can think of this as 
searching level by level out from A. An interative solution involving a queue usually works best.
"""

from Queue import Queue


def bfs_search(root):
    queue = Queue()
    root.marked = True
    queue.queue(root)  # adds to the end of queue

    while not queue.empty():
        node = queue.get()

        visit(node)

        for each_node in node.adjacent:

            if each_node.marked is False:
                each_node.marked = True
                queue.queue(each_node)


"""
    If asked to implement BFS, the key thing to remember sis the use of the queue. The rest of the algorithms flows
from this fact. 
"""