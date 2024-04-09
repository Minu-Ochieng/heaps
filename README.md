A heap is a unique kind of tree data structure. Typically, a heap tree is either a max-heap tree, where all parent nodes are larger than their children, or a min-heap tree, where each parent node is less than its children.
Advantages of using heap
Space efficiency: Because the heap data structure stores elements in a complete binary tree structure, it uses less memory than alternative data structures like linked lists or arrays.
Disadvantages of using heap
Lack of flexibility: Because the heap data structure is meant to preserve a particular elemental order, it is not highly flexible. This implies that some applications that call for more flexible data structures might find it unsuitable.

Application of binary tree

Job scheduling
Priority Queues
Graph Algorithms
Heapsort algorithm

Heap Property

The heap property says that is the value of Parent is either greater than or equal to (in a max heap ) or less than or equal to (in a min heap) the value of the Child.
A heap is described in memory using linear arrays in a sequential manner.
Shape Property
Complete binary tree

Accessing items in a heap

Items in this data structure are accessed by the heap module, where each time the item is popped or pushed the heap structure is maintained. 
Adding items in a heap
Heappush(): function used to insert items mentioned in its argument in a heap
Removing items from a heap
Heappop(): function used to remove and return the smallest item in a heap

