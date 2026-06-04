public class IntList {
    int first;
    IntList rest;

    public IntList(int f, IntList r) {
        first = f;
        rest = r;
    }

    /** Return the size of the list using... recursion! */
    public int size() {
        if (rest == null) {
            return 1;
        }
        return 1 + this.rest.size();
    }

    /** Return the size of the list using no recursion! */
    public int iterativeSize() {
        IntList p = this;
        int totalSize = 0;
        while (p != null) {
            totalSize += 1;
            p = p.rest;
        }
        return totalSize;
    }

    /** Returns the ith item of this IntList. */
    public int get(int i) {
        if (i == 0) {
            return first;
        }
        return rest.get(i - 1);
    }

    /** Return a new list with the same ints, but incremented by 1. */
    public IntList incrementRecursiveNonDestructive() {
        IntList incremented = new IntList(first + 1, null);
        if (rest != null) {
            incremented.rest = rest.incrementRecursiveNonDestructive();
        }
        return incremented;
    }

    /**
     * Returns an IntList identical to L, but with
     * each element incremented by x. Modifies the original list.
     * You are not allowed to use "new" in this method.
     */
    public static IntList incrRecursiveDestructive(IntList L, int x) {
        L.first += x;
        if (L.rest != null) {
            L.rest = incrRecursiveDestructive(L.rest, x);
        }
        return L;
    }

    /*
     * =================================================================
     * OPTIONAL METHODS
     * =================================================================
     */

    /**
     * Returns the sum of all elements in the IntList.
     */
    public int sum() {
        if (rest == null){
            return first;
        } else{
            return first + rest.sum();
        }
    }

    /**
     * Destructively adds x to the end of the list.
     */
    public void addLast(int x) {
        if (rest == null){
            rest = new IntList(x, null);
        } else {
            rest.addLast(x);
        }
    }

    /**
     * Destructively adds x to the front of this IntList.
     * This is a bit tricky to implement. The standard way to do this would be
     * to return a new IntList, but for practice, this implementation should
     * be destructive.
     */
    public void addFirst(int x) {
        rest = new IntList(first, rest);
        first = x;
    }

    public static void main(String[] args) {
        IntList L = new IntList(5, null);
        L.rest = new IntList(7, null);
        L.rest.rest = new IntList(9, null);

        IntList M = incrRecursiveDestructive(L, 3);
        System.out.println(L.sum());
        L.addLast(5);
        L.addFirst(2);
        System.out.println(L.sum());
        System.out.println(L.first);
        System.out.println(M.sum());
   }
}


