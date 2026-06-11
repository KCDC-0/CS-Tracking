## Graphs

Graphs are versatile structures consisting of a collection of vertices (nodes) connected by edges. Unlike trees, they do not require hierarchical relationships.

Simple graphs follow 2 rules:
- No loops: A vertex cannot connect to itself
- No parallel edges: There cannot be multiple edges connecting the same two vertices

<br>

Graphs can be categorized by several key characteristics:
- Directed vs. Undirected: Edges either have a specific direction or can be traversed in any direction
- Cyclic vs. Acyclic: Cyclic graphs contain paths that form a loop
- Weighted/Labeled: Edges can have labels (eg: distances), and vertices can have weights
- Connected: A graph is connected if a path exists to travel from any vertex to any other vertex

<br>

Many foundational computer science and AI algorithms rely heavily on graph structures, such as: Depth First Search (DFS), Breadth First Search (BFS), Minimum Spanning Trees, Shortest Paths, Dijkstra’s Algorithm, A* Search, Prim’s Algorithm, and Kruskal’s Algorithm.

Other problems include: Pathfinding & routing, detecting cycles, checking overall connectivity,  identifying single points of failure, checking if two graphs are isomorphic, or if a graph is planar, or finding paths that visit every vertex or edge exactly once

<br>
<br>

## Hashing

To achieve fast searching of Θ(1) time, we can a massive array allows instant access to elements based on their index, but it consumes an impractical amount of memory.

Thus, we can use hash codes which map a large universe of potential data into a smaller, memory-efficient set of storage buckets. However, poorly distributed hash codes place too many items in the same bucket, turning them into linked lists and degrading search runtime from O(1) to O(n).

Here are some features of good hash codes:
- Consistency: Objects that are considered equal must generate the exact same hash code
- Distribution: The function must generate a wide variety of codes to distribute items evenly across all available buckets
- Unpredictability: There should be no distinguishable patterns in the hash codes of different objects

This generation is natively handled by the hashCode() function in Java's Object class

<br>

To prevent overcrowding, hash tables increase their bucket count based on a load ratio, calculated as items divided by buckets (N/M). When a table resizes, all items must have their hash codes recomputed to rebalance the storage buckets. Spreading the cost of this operation over time ensures the amortized runtime remains Θ(1).

<br>

In Java, hash tables are used in the data structures HashSet and HashMap which are the most popular implementation of sets and maps. These implementations offer excellent performance and do not require values to be inherently comparable. However, objects must not be modified after insertion; mutating an object alters its hash code, effectively causing the table to lose track of it.

<br>
<br>

## Comparables and Comparators

A comparable is a generic interface that enables standardized comparisons between objects, widely used in Java libraries


