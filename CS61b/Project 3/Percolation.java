import edu.princeton.cs.algs4.WeightedQuickUnionUF;

public class Percolation {
    private final boolean[][] grid;
    private final int size;
    private int openSitesCount;

    // Disjoint set tracking to check for percolation (Includes Virtual Top and Bottom)
    private final WeightedQuickUnionUF ufWithBottom;
    // Disjoint set tracking to prevent backwash (Includes Virtual Top only)
    private final WeightedQuickUnionUF ufWithoutBottom;

    private final int virtualTopIndex;
    private final int virtualBottomIndex;

    // Task 1: Constructor
    public Percolation(int N) {
        if (N <= 0) {
            throw new IllegalArgumentException("Grid size N must be greater than 0.");
        }
        this.size = N;
        this.grid = new boolean[N][N];
        this.openSitesCount = 0;

        int totalNodes = N * N;
        this.virtualTopIndex = totalNodes;
        this.virtualBottomIndex = totalNodes + 1;

        this.ufWithBottom = new WeightedQuickUnionUF(totalNodes + 2);
        this.ufWithoutBottom = new WeightedQuickUnionUF(totalNodes + 1);
    }

    private int xyTo1D(int row, int col) {
        return (row * size) + col;
    }

    private void validateBounds(int row, int col) {
        if (row < 0 || row >= size || col < 0 || col >= size) {
            throw new IndexOutOfBoundsException("Index out of bounds mapping.");
        }
    }

    // Task 1 & 2: open the site (row, col)
    public void open(int row, int col) {
        validateBounds(row, col);

        if (grid[row][col]) {
            return;
        }

        grid[row][col] = true;
        openSitesCount++;

        int current1D = xyTo1D(row, col);

        if (row == 0) {
            ufWithBottom.union(current1D, virtualTopIndex);
            ufWithoutBottom.union(current1D, virtualTopIndex);
        }

        if (row == size - 1) {
            ufWithBottom.union(current1D, virtualBottomIndex);
        }

        int[][] neighbors = {
            {row - 1, col}, // Up
            {row + 1, col}, // Down
            {row, col - 1}, // Left
            {row, col + 1}  // Right
        };

        for (int[] neighbor : neighbors) {
            int r = neighbor[0];
            int c = neighbor[1];
            
            if (r >= 0 && r < size && c >= 0 && c < size && grid[r][c]) {
                int neighbor1D = xyTo1D(r, c);
                ufWithBottom.union(current1D, neighbor1D);
                ufWithoutBottom.union(current1D, neighbor1D);
            }
        }
    }

    // Task 1: Check if the site is open
    public boolean isOpen(int row, int col) {
        validateBounds(row, col);
        return grid[row][col];
    }

    // Task 1 & 2: Check if site is full (handles backwash by using ufWithoutBottom)
    public boolean isFull(int row, int col) {
        validateBounds(row, col);
        if (!isOpen(row, col)) {
            return false;
        }
        return ufWithoutBottom. someConnected(xyTo1D(row, col), virtualTopIndex);
    }

    private static class WeightedQuickUnionUFBridge extends WeightedQuickUnionUF {
        public WeightedQuickUnionUFBridge(int n) {
            super(n);
        }
    }

    private boolean someConnected(int p, int q) {
        return ufWithoutBottom.connected(p, q);
    }

    // Task 1: Returns total open items
    public int numberOfOpenSites() {
        return openSitesCount;
    }

    // Task 1: Does the system percolate?
    public boolean percolates() {
        return ufWithBottom.connected(virtualTopIndex, virtualBottomIndex);
    }
}