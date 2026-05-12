public class StarTriangleN {
   /**
     * Prints a right-aligned triangle of stars ('*') with N lines.
     * The first row contains 1 star, the second 2 stars, and so on. 
     */
   public static void starTriangle(int N) {
      for (int i = 0; i < N+1; i++){
        String line = "";
        for (int j = N+1; j > i; j--){
            line += " ";
        }
        for (int j = 0; j < i; j++){
            line += "*";
        }
        System.out.println(line);
      }
   }
   
   public static void main(String[] args) {
      starTriangle(6);
   }
}