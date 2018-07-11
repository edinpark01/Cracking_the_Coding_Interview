"""
A hash table is a data structure that maps keys to values for highly efficient lookup.
There are a number of ways of implementing this. Here, we will describe a simple but common implementation.

We will use an array of linked lists and a hash code function. To insert a key (which might be a string or
essentially any other data type) to a value.
"""


# STEP 1:   Compute the key's hash code, which will usually be an int or long. Note that two different keys could
#           have the same hash code, as there may be an infinite number of keys and a finite number of ints.


# STEP 2:   Map the hash code to an index in the array. This could be done with something like a
#           hash (key) % array_length. Two different hash codes could of course map to the same index.

# STEP 3:   At this index, there is a linked list of keys and values. Store the key and value in this index.
#           We must use a linked list because of collisions: you could have two different keys with the same
#           hash code, OR two different hash codes that map to the same index.

# STEP 4:   RETRIEVAL -> repeat the process.
#           STEP 1: Compute the hash code from the key
#           STEP 2: Compute the index from the hash code
#           STEP 3: Search through the linked list for the value with this key

#   Worse case: If the number of collisions is very high, the worse case runtime is O(n),
#               where n is the number of keys.
#   Best case:  Assume a good O(1) implementation, which maintains the collisions to a minimum.

# NOTE: We may use a balanced binary search tree for a hash table which gives us an O(log N) lookup time.
#       ADVANTAGE: potentially using less space AND also iterate though the keys in order, which can be useful.

