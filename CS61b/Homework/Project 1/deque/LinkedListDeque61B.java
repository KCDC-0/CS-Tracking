
package deque;

import java.util.List;
import java.util.ArrayList;

public class LinkedListDeque61B<T> implements Deque61B<T> {

    private class Node {
        public T item;
        public Node prev;
        public Node next;

        public Node(T item, Node prev, Node next) {
            this.item = item;
            this.prev = prev;
            this.next = next;
        }
    }

    private Node sentinel;
    private int size;

    // Task 3: Constructor
    // Creates an empty circular deque with a single sentinel node
    public LinkedListDeque61B() {
        sentinel = new Node(null, null, null);
        sentinel.prev = sentinel;
        sentinel.next = sentinel;
        size = 0;
    }

    // Task 4: addFirst
    @Override
    public void addFirst(T item) {
        Node newNode = new Node(item, sentinel, sentinel.next);
        sentinel.next.prev = newNode;
        sentinel.next = newNode;
        size += 1;
    }

    // Task 4: addLast
    @Override
    public void addLast(T item) {
        Node newNode = new Node(item, sentinel.prev, sentinel);
        sentinel.prev.next = newNode;
        sentinel.prev = newNode;
        size += 1;
    }

    // Task 5: toList
    @Override
    public List<T> toList() {
        List<T> returnList = new ArrayList<>();
        Node current = sentinel.next;
        while (current != sentinel) {
            returnList.add(current.item);
            current = current.next;
        }
        return returnList;
    }

    // Task 6: isEmpty
    @Override
    public boolean isEmpty() {
        return size == 0;
    }

    // Task 6: size
    @Override
    public int size() {
        return size;
    }

    // Task 7: getFirst
    @Override
    public T getFirst() {
        if (isEmpty()) {
            return null;
        }
        return sentinel.next.item;
    }

    // Task 7: getLast
    @Override
    public T getLast() {
        if (isEmpty()) {
            return null;
        }
        return sentinel.prev.item;
    }

    // Task 8: get (Iterative)
    @Override
    public T get(int index) {
        if (index < 0 || index >= size) {
            return null;
        }
        Node current = sentinel.next;
        for (int i = 0; i < index; i++) {
            current = current.next;
        }
        return current.item;
    }

    // Task 8: getRecursive
    @Override
    public T getRecursive(int index) {
        if (index < 0 || index >= size) {
            return null;
        }
        return getRecursiveHelper(sentinel.next, index);
    }

    private T getRecursiveHelper(Node node, int index) {
        if (index == 0) {
            return node.item;
        }
        return getRecursiveHelper(node.next, index - 1);
    }

    // Task 9: removeFirst
    @Override
    public T removeFirst() {
        if (isEmpty()) {
            return null;
        }
        Node firstNode = sentinel.next;
        T item = firstNode.item;
        
        sentinel.next = firstNode.next;
        firstNode.next.prev = sentinel;
        
        size--;
        return item;
    }

    // Task 9: removeLast
    @Override
    public T removeLast() {
        if (isEmpty()) {
            return null;
        }
        Node lastNode = sentinel.prev;
        T item = lastNode.item;
        
        sentinel.prev = lastNode.prev;
        lastNode.prev.next = sentinel;
        
        size--;
        return item;
    }
        public static void main(String[] args) {
                Deque61B<Integer> lld = new LinkedListDeque61B<>();
                lld.addLast(0);   // [0]
                lld.addLast(1);   // [0, 1]
                lld.addFirst(-1); // [-1, 0, 1]
        }
}

