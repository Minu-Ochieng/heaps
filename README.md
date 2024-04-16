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




**Tupple**
A tuple is a group of items that are divided up with commas. A tuple and a list are similar in several characteristics such as indexing, nested items, and repetition; Even so, the main difference between the two is that a tuple is immutable, while a list is mutable.
Tuples are ordered, immutable, and allow duplicates.

**Advantages of Tuple**
1.The values and arrangement of tuples are fixed.
2.Tuples are faster than list
3.The code is protected from unintentional changes using tuples. It is preferable to store data in "tuples" rather than "lists" when it is needed for a program that shouldn't be altered.
4.A tuple containing strings, numbers, or another tuple that contains immutable values can be used as a dictionary key.

**Disadvantages**
1.Since tuples are immutable, once they are created, they cannot be modified.
2.Few Operations -Compared to lists, tuples have fewer built-in operations. For instance, you are unable to sort, add, or remove elements from a tuple.

**Properties of Tuple**
They're immutable.
They can have duplicate items in them.
They have an index.
Tuples are ordered

**Accessing An Item in a Tuple**
One can access a tuple using indexing where the first element is index 0
Example:
class=("Adalab","Anitab","Lovelace")
class[1]

**Adding an element to a Tuple**
Tuples are immutable so you cant add items 

**Removing an element to a Tuple**
Tuples are immutable so you cant remove items

**Some operations used on Tuple**
Concatenate 
One can concatenate using + operator
**Tuple operations**
