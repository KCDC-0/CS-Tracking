package deque;

import java.util.List;
import java.util.ArrayList;
import java.util.Iterator;

public class ArrayDeque61B<T> implements Deque61B<T>, Iterable<T> {
    private T[] items;
    private int size;
    private int nextFirst;
    private int nextLast;

    private static final int INITIAL_CAPACITY = 8;
    private static final double MIN_USAGE_FACTOR = 0.25;

    // Task 2: Constructor
    public ArrayDeque61B() {
        items = (T[]) new Object[INITIAL_CAPACITY];
        size = 0;
        nextFirst = 4; // Arbitrary starting position 
        nextLast = 5;  // Right next to nextFirst
    }

    private int floorMod(int x, int m) {
        int r = x % m;
        return r < 0 ? r + m : r;
    }

    // Task 9 & 10: Resizing Helper
    private void resize(int capacity) {
        T[] newArray = (T[]) new Object[capacity];
        int current = floorMod(nextFirst + 1, items.length);
        
        for (int i = 0; i < size; i++) {
            newArray[i] = items[current];
            current = floorMod(current + 1, items.length);
        }
        
        items = newArray;
        nextFirst = capacity - 1;
        nextLast = size;
    }

    private void checkResize() {
        if (size == items.length) {
            resize(items.length * 2); // Resize up (Geometric factor 2x)
        } else if (items.length >= 16 && (double) size / items.length <= MIN_USAGE_FACTOR) {
            resize(items.length / 2); // Resize down
        }
    }

    // Task 3: addFirst
    @Override
    public void addFirst(T item) {
        checkResize();
        items[nextFirst] = item;
        nextFirst = floorMod(nextFirst - 1, items.length);
        size++;
    }

    // Task 3: addLast
    @Override
    public void addLast(T item) {
        checkResize();
        items[nextLast] = item;
        nextLast = floorMod(nextLast + 1, items.length);
        size++;
    }

    // Task 7: toList
    @Override
    public List<T> toList() {
        List<T> resultList = new ArrayList<>();
        int current = floorMod(nextFirst + 1, items.length);
        for (int i = 0; i < size; i++) {
            resultList.add(items[current]);
            current = floorMod(current + 1, items.length);
        }
        return resultList;
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

    // Task 4: getFirst
    @Override
    public T getFirst() {
        if (isEmpty()) {
            return null;
        }
        return items[floorMod(nextFirst + 1, items.length)];
    }

    // Task 4: getLast
    @Override
    public T getLast() {
        if (isEmpty()) {
            return null;
        }
        return items[floorMod(nextLast - 1, items.length)];
    }

    // Task 5: get
    @Override
    public T get(int index) {
        if (index < 0 || index >= size) {
            return null;
        }
        int actualIndex = floorMod(nextFirst + 1 + index, items.length);
        return items[actualIndex];
    }

    // Task 5: getRecursive
    @Override
    public T getRecursive(int index) {
        throw new UnsupportedOperationException("No need to implement getRecursive for ArrayDeque61B.");
    }

    // Task 8: removeFirst
    @Override
    public T removeFirst() {
        if (isEmpty()) {
            return null;
        }
        int firstIndex = floorMod(nextFirst + 1, items.length);
        T item = items[firstIndex];
        items[firstIndex] = null; // Clear reference for garbage collection
        nextFirst = firstIndex;
        size--;
        checkResize();
        return item;
    }

    // Task 8: removeLast
    @Override
    public T removeLast() {
        if (isEmpty()) {
            return null;
        }
        int lastIndex = floorMod(nextLast - 1, items.length);
        T item = items[lastIndex];
        items[lastIndex] = null; // Clear reference for garbage collection
        nextLast = lastIndex;
        size--;
        checkResize();
        return item;
    }

    // Task 12: Iterator Support
    @Override
    public Iterator<T> iterator() {
        return new ArrayDequeIterator();
    }

    private class ArrayDequeIterator implements Iterator<T> {
        private int pos = 0;

        @Override
        public boolean hasNext() {
            return pos < size;
        }

        @Override
        public T next() {
            T item = get(pos);
            pos++;
            return item;
        }
    }

    // Task 13: equals
    @Override
    public boolean equals(Object o) {
        if (this == o) {
            return true;
        }
        if (o instanceof Deque61B<?> otherDeque) {
            if (this.size != otherDeque.size()) {
                return false;
            }
            for (int i = 0; i < this.size; i++) {
                if (!this.get(i).equals(otherDeque.get(i))) {
                    return false;
                }
            }
            return true;
        }
        return false;
    }

    // Task 14: toString
    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder("[");
        for (int i = 0; i < size; i++) {
            sb.append(get(i));
            if (i < size - 1) {
                sb.append(", ");
            }
        }
        sb.append("]");
        return sb.toString();
    }
}