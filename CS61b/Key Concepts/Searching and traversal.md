# Searching

## Binary search

Binary search is a way of finding a specific node in a tree. It only works on binary trees due to its helpful sorted property. It simply traverses the tree, moving left if the current node is too large or right if it is too small. Thus, it runs in O(logn) time for bushy trees.


```
public BST find(BST T, Key sk) {
    if (T == null) {
        return null;
    }
    if (sk.equals(T.key)) {
        return T;
    } else if (sk < T.key) {
        return find(T.left, sk);
    } else {
        return find(T.right, sk);
    }
}
```
<br>

## Breadth first search

Traversal is the act of visiting nodes in a specific order, applicable in trees and graphs.

BFS visits all children before any subgraphs when traversing a tree

<br>

## Depth first search

There are 3 main implementations of DFS in trees:
- Inorder traversal: visits all left children, then the node itself, then all right children, thus visiting the nodes in sorted order
- Preorder traversal: visits the node itself first, then all left children, then all right children, useful for printing a directory tree structure.
- Postorder traversal: visits all left children, then all right children, then finally the node itself. This is needed when operations need to be done on all children before the result can be read in the node.

Here's how they might look:
```
void inOrder(Node x) {
    if (x == null) return;
    inOrder(x.left);
    print(x);
    inOrder(x.right);
}

void preOrder(Node x) {
    if (x == null) return;
    print(x);
    preOrder(x.left);
    preOrder(x.right);
}

void postOrder(Node x) {
    if (x == null) return;
    preOrder(x.left);
    preOrder(x.right);
    print(x);
}
```

<br>
<br>

# Shortest path


## Dikstra's Algorithm

Dijkstra’s Algorithm (also known as Uniform Cost Search in state-space contexts) finds the shortest path from a source vertex to all other vertices in a graph. It operates by systematically visiting vertices in order of their best-known distance from the source.

Here are some invariant data structures present in this implementation
- Priority Queue (PQ): Maintains all unvisited vertices, ordered by their current shortest known distance (distTo)
- distTo array: Tracks the shortest calculated distance from the source to every other vertex
- edgeTo array: Records the best known predecessor vertex to trace the shortest path back to the source

In this algorithm relaxing is the process of checking if traveling through the currently visited node provides a shorter path to a neighboring node.

If the new path distance is smaller than the neighbor's current distTo value, the algorithm updates the neighbor's distTo, sets its edgeTo to the current node, and updates its priority in the PQ.

<br>

Here are the algorithm steps:
- Initialize: Set the source vertex distance to 0 and all other vertices to infinity. Add all to the PQ.
- Select: Remove the vertex with the smallest distance from the PQ.
- Relax: Relax all outgoing edges of the selected vertex.
- Repeat: Continue removing the smallest vertex and relaxing its edges until the PQ is empty.


```
public Class Djikstra() {

    public Djikstra() {
        PQ = new PriorityQueue<>();
        distTo = new Distance[numVertices];
        edgeTo = new Edge[numVertices];
    }

    public void doDijkstras(Vertex sourceVertex) {
        PQ.add(sourceVertex, 0);
        for(v : allOtherVertices) {
            PQ.add(v, INFINITY);
        }
        while (!PQ.isEmpty()) {
            Vertex p = PQ.removeSmallest();
            relax(p);
        }
    }
    // Relaxes all edges of p
    void relax(Vertex p) {
        for (q : p.neighbors()) {
            if (distTo[p] + q.edgeWeight < distTo[q]) {
                distTo[q] = distTo[p] + q.edgeWeight;
                edgeTo[q] = p;
                PQ.changePriority(q, distTo[q]);
            }
        }
    }
}
```

The simplified runtime for this is $\Theta(E \log V)$

<br>

## A* algorithm

A* is essentially Dijkstra’s Algorithm enhanced with a heuristic function. This heuristic function calculates weights of a path from a vertex to a goal vertex. ertices are visited based on the lowest combined value of distance + heuristic. It does not necessarily visit every vertex in the graph.

Here are some properties of a goof heuristic:
- Admissible: heuristic of each vertex returns a cost that is <= the true cost/distance i.e. h(A) <= cost(A, goal)
- Consistent: difference between heuristics of two vertices <= true cost between them i.e. h(A) - h(B) <= cost(A, B)
