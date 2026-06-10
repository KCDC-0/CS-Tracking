## Intro

Binary trees evolve from the concept of linked lists by placing pointers at the center of sublists rather than the ends, creating a hierarchical structure. All trees consist of a root node and nodes that point to child nodes. Nodes with no children are called leaves.


A Binary Search Tree (BST), is such that each node has at most two children. For any given node, all values in its left subtree are smaller, and all values in its right subtree are greater. Values are transitive, unique (no duplicates), complete (all values are comparable), and antisymmetric.

<br>

## Operations

The 3 main operations that binary trees should support are:
- Find: Finding a value in a tree uses the Binary Search algorithm
- Insert: Searches for the target item. If found, it does nothing. If not found, a new leaf node is created and placed in the correct sorted position.
- Delete: Case A (Leaf): The node is simply removed. Case B (One child): The node is swapped with its child and then deleted. Case C (Two children): The node is swapped with the next largest value in its subtrees (the successor) before deletion.


The runtime of tree operations is heavily dependent on the tree's shape. The best case is where every parent has exactly two children. The height is bounded at $\Theta(\log n)$, guaranteeing $\Theta(\log n)$ runtime for search and insertion. When every parent has only one child, structurally mimicking a linked list, the height degrades to $\Theta(n)$, resulting in $\Theta(n)$ operational runtimes.

<br>

## B Trees

B Trees optimize search by allowing nodes to hold multiple values and possess multiple children. Parent nodes can have 2 to 4 children. New values are placed in existing children. If a node reaches its maximum capacity (e.g., 3 values), it splits: one value moves up to the parent, and a new child node is created.

Herea are some key properties:
- Searching within a single node takes constant time due to strict limits on node size
- All leaf nodes are exactly the same distance from the root
- A non-leaf node containing $k$ items must have exactly $k+1$ children
- The height of the tree is strictly $\Theta(\log n)$.

<br>

Red-Black Trees represent B Trees within a standard binary tree format (maximum of 2 children per parent) by introducing a color property.

Black nodes function as standard binary tree nodes. Red nodes logically group with their parent to represent the multi-value nodes found in B Trees. To simplify implementation, these trees are often restricted to "Left-Leaning Red-Black Trees" (LLRB), meaning red links are only allowed on the left child. Structural adjustments (left and right rotations) that swap nodes to maintain valid binary and Red-Black tree properties during insertion. For example, a left rotation moves a right child up and to the left to replace its parent.

Red Black trees have a one-to-one correspondence with B trees, and every path from a node to the root contains the exact same number of black nodes.

Here is how insertion would work in red black trees:
Always insert new values as red leaf nodes. Rotate left if a right-leaning red link is created. Rotate right if two consecutive left-leaning red links exist. Temporarily allow a node to have red links on both sides, then "color flip" to resolve it (pushing the red link up the tree).

<br>

## Heaps

A heap is a specific order for storing data, usually in a list, that resembles a binary tree. Unlike standard trees, heaps primarily care about the root node, which holds either the largest value (max-heap) or the smallest value (min-heap). Every element must be larger than all its children (in a max-heap) or smaller than all its children (in a min-heap). A parent node's index can be calculated using floor division: parentIndex = nodeIndex / 2.

To convert an array into a heap, start at the middle element of the array. If the element is smaller than either of its children, swap it with the largest child. If a swap occurs, recursively call the conversion function on the new position. If no swap is needed, end the recursion.

he heap structure is the foundation of Heap Sort, an algorithm that provides consistent sorting at a speed of nlogn.

<br>

## Tries

A trie is a specific implementation of a set and is short for retrieval tree. It is a specific set implementation designed for collections with a finite alphabet, where nodes act as arrays containing all characters in the alphabet, enabling extremely fast branching via direct indexing.

This implementation allows for certain methods such as the add() and contains() functions run in $\Theta(1)$ time.

<br>

## Method complexity summary

| Methods | Ordered Array | Bushy BST | Hash Table | Heap |
| -------- | -------- | -------- | -------- | -------- |
| add | Θ(N) | Θ(logN) | Θ(1) | Θ(logN) |
| getSmallest | Θ(1) | Θ(logN) | Θ(N) | Θ(1) |
| removeSmallest | Θ(N) | Θ(logN) | Θ(N) | Θ(logN) |


