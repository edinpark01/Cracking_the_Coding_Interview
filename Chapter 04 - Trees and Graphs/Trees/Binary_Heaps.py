"""
    BINARY HEAPS
    We will discuss min-heaps here. Mas-heaps are essentially equivalent, but the elements are in descending
order rather than ascending order.
    A min-heap is a complete binary tree (that is, totally filled other than the rightmost elements on the last level)
where each nde is smaller that its children. The root, therefore, is the minimum element in the tree.
"""
"""
                [ 7 ]
               /     \ 
              /       [ 87 ]  
             /
        [ 4 ] 
             \      
              \        [ 90 ]
               \      /
                [ 50 ]
                      \ 
                       [ 55 ]

    We have two key operations on a min-heap. INSERT & EXTRACT MIN
    
    INSERT
    When we insert into a min-heap, we always start by inserting the element at the bottom. We insert at the rightmost
spot so as to maintain the complete tree property.
    Then, we "fix" the tree by swapping the new element with its parent, until we find an appropriate sport for the
element. We essentially bubble up the minimum element.

    EXTRACT MINIMUM ELEMENT
    Finding the minimum element of a min-heap is easy; it is always at the top. The trickier part is how to remove it. 
    
    1. Remove the minimum element and swap it with the last element in the heap (the bottommost rightmost element).
    2. Bubble down this element, swapping it with one of tis children until the min-heap property is restored. 
    
    Do we swap it with the left child or the right child? That depends on their values. 
    There's no inherent ordering between the left and right element, but you will need to take the smaller one 
in order to maintain the min-heap ordering.
"""