public class StarTriangle5 {
   /**
     * Prints a right-aligned triangle of stars ('*') with 5 lines.
     * The first row contains 1 star, the second 2 stars, and so on. 
     */
   public static void starTriangle5() {
      for (int i = 0; i < 6; i++){
        String line = "";
        for (int j = 6; j > i; j--){
            line += " ";
        }
        for (int j = 0; j < i; j++){
            line += "*";
        }
        System.out.println(line);
      }
   }
   
   public static void main(String[] args) {
      starTriangle5();
   }
}