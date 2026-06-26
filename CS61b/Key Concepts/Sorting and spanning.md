# Minimum spanning trees

A spanning tree (T) is a subgraph of a graph (G) that must possess three properties:
- Connected: There is a path to every vertex
- Acyclic: It contains no cycles
- Spanning: It includes every vertex in the graph.


A Minimum Spanning Tree (MST) is a spanning tree that has the lowest possible total edge weight.

An MST is a global property of the entire graph and has no source node. Conversely, an SPT depends on a specific starting source node (like a Dijkstra's algorithm solution). Although under certain conditions, it is possible for an MST and an SPT to be the exact same tree.

<br>

A cut is a division of a graph's nodes into two distinct sets, and a crossing edge is an edge connecting a node in one set to a node in the other.

The Cut Property Rule states that no matter how a cut is made, the crossing edge with the smallest weight will always be included in the MST.


<br>

## Kruskal's algorithm


Kruskal’s algorithm is one optimal way to construct a MST. These are the steps:
1. Sort all graph edges in order of increasing weight
2. Continually add the smallest available edge to the MST unless it creates a cycle
3. Stop when the MST contains exactly $V - 1$ edges ($V$ being the number of vertices)

Time complexity is $\Theta(E\log(E))$

<br>

Unlike Prim's Algorithm, Kruskal's does not guarantee a single, continuous tree structure while running. It connects disjoint sets step-by-step until they form a single spanning tree at the very end.


```
public class Kruskals() {

    public Kruskals() {
        PQ edges = new PriorityQueue<>();
        ArrayList<Edge> mst = new ArrayList<>();
    }

    public void doKruskals(Graph G) {
        for (e : G.edges()) {
            PQ.add(e);
        }
        WeightedQU uf = new WeightedQU(G.V());
        Edge e = PQ.removeSmallest();
        int v = e.from();
        int w = e.to();
        if (!uf.isConnected(v, w)) {
            uf.union(v, w);
            mst.add(e);
        }

    }
}

```

<br>

## Prim's algorithm

Prim’s algorithm is another optimal way to construct an MST.

The algorithm starts at an arbitrary vertex. It repeatedly examines all immediate neighbors of the current MST and adds the edge with the smallest weight that connects a visited node to an unvisited node.

All vertices are added to the PriorityQueue, ordered by their distance from the MST (initially set to infinity, except for the source which is 0). The vertex with the highest priority (smallest distance) is iteratively removed and marked as visited. Its edges are "relaxed" if an unvisited neighbor's edge weight is smaller than its currently recorded distance, its distTo and edgeTo values are updated, and its priority in the queue is adjusted.

```
public class Prims() {

    public Prims() {
        PQ = new PriorityQueue<>();
        edgeTo = new Edge[numVertices];
        distTo = new Dist[numVertices];
        marked = new boolean[numVertices];
    }

    public void doPrims() {
        PQ.add(sourceVertex, 0);
        for(v : allOtherVertices) {
            PQ.add(v, INFINITY);
        }
        while (!PQ.isEmpty()) {
            Vertex p = PQ.removeSmallest();
            marked[p] = true;
            relax(p);
        }
    }

    public void relax(Vertex p) {
        for (q : p.neighbors()) {
            if (marked[q]) { continue; }
            if (q.edgeWeight < distTo[q]) {
                distTo[q] = q.edgeWeigth;
                edgeTo[q] = p;
                PQ.changePriority(q, distTo[q]);
            }
        }
    }
}
```

<br>

While the structure is nearly identical to Dijkstra's, Prim's algorithm evaluates the shortest distance from the MST to a vertex, rather than the total accumulated path distance from the source vertex. Its simplified time complexity is $\theta(E \log V)$



# Sorting

Sorting is useful as it speeds up searches (e.g., enabling binary search) and avoids $\Theta(N)$ full list scans. It also makes it easy to find equivalent items by simply checking neighboring values.

Here are some sorting algorithm classifications:
- Internal sort: Keeps all data in primary memory
- External sort: Processes data in batches, then merges them together at the end
- Comparison-based sort: The only thing we know about keys are their relative orders
- Radix sort: Uses information other than keys
- Insertion sort: Insert items at their appropriate positions one at a time
- Selection sort: Chooses items and places them in order


Using the Arrays.sort method automatically selects the optimal sorting algorithm for the given list.

The number of inversions is a metric for determining how "unsorted" a list is, calculated by counting every pair of elements that are swapped compared to their proper sorted positions. A perfectly sorted list has $0$ inversions. The worst-case scenario (a completely reversed list) has $\frac{N(N-1)}{2}$ inversions.