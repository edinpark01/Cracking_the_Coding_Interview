"""
In some languages, arrays (often called lists in this case) are automatically resizable.
The array or list will grow as you append items. In other languages, like Java, arrays are fixed length.
The size is defined when you create the array.

When you need an array-like data structure that offers dynamic resizing, you would ussually use an ArrayList.
An ArrayList is an array that resizes itself as needed while still providing O(1) access. A typical implementation
that its amortized insertion time is still O(1).

This is an essential data structure for interviews. Be sure you are confortable with dynamically resizable arrays/lists
in whatever language you will be working with. NOTE: the same name of the data structure as well as the 'resizing factor'
(which is 2) may vary.

QUESTION:   Why is the amortized insertion runtime O(1)?
ANSWER:     Suppose you have an array of size N. We can work backwards to compute how many elements we copied at each
            capacity increase. Observe that when we increse the array to K elements, the array was previously
            half that size. Therefore, we need to copy k/2 elements.
"""

