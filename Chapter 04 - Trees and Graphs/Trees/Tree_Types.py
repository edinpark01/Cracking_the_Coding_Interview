"""
    A nice way to understand a tree is with a recursive explanation. A tree is a data structure composed of
nodes.
    - Each tree has a root Node. (Actually, this is not strictly necessary in graph theory, but it is usually
how we use trees in programming, and especially programming interviews.)
    - The root node has zero or more child nodes.
    - Each child node has zero or more child nodes, and so on.

"""


class Node:  # Very simple class definition for Node:
    def __init__(self):
        self.name = None  # type String
        self.children = []


class Tree:  # Tree class to wrap node.
    def __init__(self):
        self.root = None


"""
    TREES vs BINARY TREES
    A binary tree is a tree in which each node has up to two children. Not all trees are binary trees. 
                 
                 [ 2 ]              This is a ternary tree, not a binary tree. 
                / 
           [ 4 ] -- [ 1 ]        
          /        
    [ 8 ] -- [ 6 ]
          \ 
           [ 10 ]
                  \ 
                   [ 20 ] <- A node is called a 'leaf' if it has no children. 
    
    There are occasions when you might have a tree that is not a binary tree. For example, suppose you were 
using a tree to represent a bunch of phone numbers. In this case, you might use a 10-are tree, with each node having up 
to 10 children. (one for each digit).

    BINARY TREE vs BINARY SEARCH TREE
    A binary search tree is a binary tree in which every node fits a specific ordering properly:
    
                all left descendants <= n < all right descendants. THIS MUST BE TRUE FOR EACH NODE n
    
    Note that this inequality must be true for all of a node's descendants, not just it is immediate children. The 
following tree on the left below is a binary search tree. The tree on the right is not, since 12 is to the left of 8.
        
                 BINARY SEARCH TREE                             NOT BINARY SEARCH TREE
                 
                         [ 2 ]                                               [ 2 ]
                        /                                                   /
                   [ 10 ]                                              [ 4 ]
                  /                                                   /     \ 
            [ 8 ]        [ 6 ]                                   [ 8 ]       [ 12 ]
                  \     /                                             \ 
                   [ 4 ]                                               [ 10 ]
                        \                                                    \ 
                         [ 2 ]                                                [ 20 ]
 
    When a given tree question, many candidates assume the interviewer means a binary search tree. Be sure to ask.
A binary search tree imposes the condition that, for each node, its left descendants are less than or equal to the 
current node, which is less than the right descendants.


    BALANCED vs UNBALANCED
    While many trees are balanced, not all are. Ask your interviewer for clarification here. Note that balancing a tree 
does not mean the left and right subtrees are exactly the same size (like you see under "perfect binary tree" in the
following diagram)
    One way to think about it is that a "balanced" tree really means something more like "not terribly imbalanced."
It is balanced enough to ensure O( log n ) times to insert and find, but it is not necessarily as balanced as it
could be.
    Two common types of balanced trees are red-black trees and  AVL trees.
    
    
    COMPLETE BINARY TREE
    A complete binary tree is a binary tree in which every level of the tree is fully filled, except for perhaps 
the last level. To the extent that the last level is filled, it is filled left to right.

            NOT A COMPLETE BINARY TREE                             A COMPLETE BINARY TREE
    
                          [ 30 ]                                              
                         /                                                    
                   [ 20 ]                                               [ 20 ]
                  /                                                    /      \ 
            [ 10 ]       [ 7 ]                                   [ 10 ]        [ 15 ]
                  \     /                                              \       [ 7 ]
                   [ 5 ]                                                \     / 
                        \                                                [ 5 ]  
                         [ 3 ]                                                \ 
                                                                               [ 3 ]
                                                                               
                                                                               
    FULL BINARY TREES
    A Perfect binary tree is one that is both full and complete. All leaf nodes will be at the same level, 
and this level has the maximum number of nodes

            NOT A FULL BINARY TREE                              A FULL BINARY TREE
    
                            [ 7 ]                                           [ 7 ]
                           /                                               /
                     [ 20 ]       [ 9 ]                              [ 20 ]       [ 9 ]
                    /      \     /                                  /      \     /
                   /        [ 3 ]                                  /        [ 3 ]
                  /              \                                /              \ 
            [ 10 ]                [ 18 ]                    [ 10 ]                [ 18 ]
                  \                                               \    
                   \       [ 12 ]                                  \ 
                    \     /                                         \ 
                     [ 5 ]                                           [ 5 ]   
                                                                     

    PERFECT BINARY TREES
    A perfect binary Trees is one that is both full and complete. All leaf nodes will be ath the same level,
and this level has the maximum number of nodes
    
                                        PERFECT BINARY TREE
    
                                                      [ 30 ]                                              
                                                     /                                                    
                                               [ 20 ]                                               
                                              /                                                    
                                        [ 10 ]       [ 7 ]                                   
                                              \     /                                              
                                               [ 5 ]                                                
                                                    \                                               
                                                     [ 3 ]
    
    Note that perfect trees are rare in interviews and in real life, as a perfect tree must have exactly 2^k -1 nodes
(where k is the number of levels). In an interview, do not assume a binary tree is perfect.
"""

