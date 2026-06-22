import java.util.Iterator;
import java.util.Objects;
import java.util.Set;
import java.util.TreeSet;
import java.util.Stack;

public class BSTMap<K extends Comparable<K>, V> implements Map61B<K, V> {

    // Helper node class to build the tree structure
    private class Node {
        K key;
        V value;
        Node left;
        Node right;

        Node(K key, V value) {
            this.key = key;
            this.value = value;
            this.left = null;
            this.right = null;
        }
    }

    private Node root;
    private int size;

    public BSTMap() {
        this.root = null;
        this.size = 0;
    }

    @Override
    public void put(K key, V value) {
        root = putHelper(root, key, value);
    }

    // Recursive helper for put
    private Node putHelper(Node node, K key, V value) {
        if (node == null) {
            size++;
            return new Node(key, value);
        }

        int cmp = key.compareTo(node.key);
        if (cmp < 0) {
            node.left = putHelper(node.left, key, value);
        } else if (cmp > 0) {
            node.right = putHelper(node.right, key, value);
        } else {
            node.value = value; // Update value if key already exists
        }
        return node;
    }

    @Override
    public V get(K key) {
        Node result = getHelper(root, key);
        return result == null ? null : result.value;
    }

    // Recursive helper for get
    private Node getHelper(Node node, K key) {
        if (node == null) {
            return null;
        }

        int cmp = key.compareTo(node.key);
        if (cmp < 0) {
            return getHelper(node.left, key);
        } else if (cmp > 0) {
            return getHelper(node.right, key);
        } else {
            return node;
        }
    }

    @Override
    public boolean containsKey(K key) {
        return getHelper(root, key) != null;
    }

    @Override
    public int size() {
        return size;
    }

    @Override
    public void clear() {
        root = null;
        size = 0;
    }

    // ----------------------------------------------------------------------
    // OPTIONAL METHODS: remove, keySet, and iterator
    // ----------------------------------------------------------------------

    @Override
    public Set<K> keySet() {
        Set<K> keys = new TreeSet<>();
        addKeys(root, keys);
        return keys;
    }

    private void addKeys(Node node, Set<K> keys) {
        if (node == null) {
            return;
        }
        addKeys(node.left, keys);
        keys.add(node.key);
        addKeys(node.right, keys);
    }

    @Override
    public V remove(K key) {
        V valueToRemove = get(key);
        if (valueToRemove != null) {
            root = removeHelper(root, key);
            size--;
        }
        return valueToRemove;
    }

    @Override
    public V remove(K key, V value) {
        V valueToRemove = get(key);
        if (valueToRemove != null && valueToRemove.equals(value)) {
            root = removeHelper(root, key);
            size--;
            return valueToRemove;
        }
        return null;
    }

    // Recursive helper for Hibbard Deletion
    private Node removeHelper(Node node, K key) {
        if (node == null) {
            return null;
        }

        int cmp = key.compareTo(node.key);
        if (cmp < 0) {
            node.left = removeHelper(node.left, key);
        } else if (cmp > 0) {
            node.right = removeHelper(node.right, key);
        } else {
            // Node to delete found
            // Case 1: No children or 1 child
            if (node.left == null) {
                return node.right;
            } else if (node.right == null) {
                return node.left;
            }

            // Case 2: Node has 2 children (Hibbard Deletion)
            Node minNode = findMin(node.right);
            node.key = minNode.key;
            node.value = minNode.value;
            node.right = removeHelper(node.right, minNode.key);
        }
        return node;
    }

    private Node findMin(Node node) {
        while (node.left != null) {
            node = node.left;
        }
        return node;
    }

    @Override
    public Iterator<K> iterator() {
        return new BSTMapIterator();
    }

    // Custom Iterator that traverses the BST in-order
    private class BSTMapIterator implements Iterator<K> {
        private Stack<Node> stack = new Stack<>();

        public BSTMapIterator() {
            pushLeftPath(root);
        }

        private void pushLeftPath(Node node) {
            while (node != null) {
                stack.push(node);
                node = node.left;
            }
        }

        @Override
        public boolean hasNext() {
            return !stack.isEmpty();
        }

        @Override
        public K next() {
            Node current = stack.pop();
            pushLeftPath(current.right);
            return current.key;
        }
    }
}