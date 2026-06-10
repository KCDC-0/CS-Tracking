for arrays, refer to 'Storing Data in Java'

## Linked Lists

Linked lists are a common form of a recursive data structure. Here are some common features of linked lists:
- Bureacracy: Create an abstraction barrier so that users do not need to know how methods work, only how to call them
- Access Control: Data cannot be accessed directly to prevent dangerous behavior, only certain methods
- Nested Class: Nodes are nested within the List object since other classes do not need it
- Caching: The size of the list is incremented every time a node is added, so running size() is O(1) and traversal is not needed
- Generalizing: A sentinel node represents an empty list and remains the first node of the list. When getFirst() is called, the second node is actually returned
- Doubly Linked: Nodes have both first and last pointers for even faster traversal
- Circular list: Sentinel last pointer points to the last value in the node, allowing for fast removeLast()

<br>

If arbitrary values need to be accessed frequently from a dataset, using arrays are much better as accessing arbitrary values from a linked list takes O(n) time.

<br>
<br>


## Stacks and queues

Stacks and queues are a another common data type. They involve pushing and popping.

Adding an item to a stack or queue is called pushing. This will either put the item on the top of a stack or in the back of a queue. On the other hand, popping is to take an item out of a stack or queue. Stacks are last in, first out, such that the last item that you put in will be the first item that gets popped. Queues are first in, first out, such that the first item that you put in will be the first item that gets popped.

Priority queues can also be implemented to order items in a queue based on priority.

<br>
<br>


## Sets

Sets are another data type that stores a collection of values with no duplicates. Common methods of sets include: add(x), contains(x), and size().

One way to implement sets is through an ArraySet, where objects get added to an array that gets resized when it’s too full. Iterators can be used to allow for iteration on top of that.

<br>

### Disjoint sets

Two sets are named disjoint sets if they have no elements in common. A Disjoint-Sets (or Union-Find) data structure keeps track of a fixed number of elements partitioned into a number of disjoint sets. In this dataset, every element starts in its own isolated subset. The main methods include:
- Union: Merges the subset containing x with the subset containing y.
- Find: Returns a boolean indicating whether x and y are currently part of the same subset.

<br>

One way to implement this is through a collection like ```List<Set<Integer>>```. However, performing a connect(x, y) operation requires iterating through up to $N$ sets to locate the elements, resulting in complex code and an $O(N)$ runtime, and would require complex implementation

Another way to implement this is through a single integer array, where the array indices represent the elements, and the array values represent the set ID that the element belongs to. Elements in the same set share the same set ID. With this, connecting 2 sets updates the array so that all elements sharing x's set ID are changed to match y's set ID (or vice versa), and checking if 2 values are connected simply checks if id[x] == id[y].

If we want to implement disjoint sets by prioritising the speed of the union operation, instead of storing a flat set ID, we could implement it such that each item in the array stores the index of its parent, essentially structuring the disjoint sets as a forest of trees. If an item has no parent, it is a root and is assigned a negative value. To connect 2 items, the roots of each item is searched and the parent of one is set to the other, the best case scenario being where both items are roots themselves. Checking if 2 items are connected can be done by checking if they have the same root. However, trees can become highly unbalanced and degenerate into long chains.

To improve upon this "quick union" implementation, we can implement it such that whenever we call connect, we always link the root of the smaller tree to the larger tree, ensuring that the maximum height of any tree is log N

We can take this further by connecting all the items along the way to the root, to make the tree shorter with each call to find. Thus, the the average runtime of connect and isConnected becomes almost constant in the long term, aka an amortised runtime.

<br>

Here is a comparison of the different implementations:


| Implementation | check if connected | connect3 |
| -------- | -------- | -------- |
| Quick Find | Θ(1) | Θ(N) |
| Quick Union | O(N) | O(N) |
| Weighted Quick Union | O(log N) | O(log N) |
| WQU with Path Compression | O(α(N))* | O(α(N))* |

α(N) tends to a constant in the long term


<br>

Here is an example implementation in java:


```
public interface DisjointSets {
    /** connects two items P and Q */
    void connect(int p, int q);

    /** checks to see if two items are connected */
    boolean isConnected(int p, int q); 
}

public class QuickFindDS implements DisjointSets {

    private int[] id;

    /* Θ(N) */
    public QuickFindDS(int N){
        id = new int[N];
        for (int i = 0; i < N; i++){
            id[i] = i;
        }
    }

    /* need to iterate through the array => Θ(N) */
    public void connect(int p, int q){
        int pid = id[p];
        int qid = id[q];
        for (int i = 0; i < id.length; i++){
            if (id[i] == pid){
                id[i] = qid;
            }
        }
    }

    /* Θ(1) */
    public boolean isConnected(int p, int q){
        return (id[p] == id[q]);
    }
}

public class QuickUnionDS implements DisjointSets {
    private int[] parent;

    public QuickUnionDS(int num) {
        parent = new int[num];
        for (int i = 0; i < num; i++) {
            parent[i] = -1;
        }
    }

    private int find(int p) {
        while (parent[p] >= 0) {
            p = parent[p];
        }
        return p;
    }

    @Override
    public void connect(int p, int q) {
        int i = find(p);
        int j= find(q);
        parent[i] = j;
    }

    @Override
    public boolean isConnected(int p, int q) {
        return find(p) == find(q);
    }
}
```

