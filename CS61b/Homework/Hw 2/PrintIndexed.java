public class PrintIndexed {
   /**
     * Prints each character of a given string followed by the reverse of its index.
     * Example: printIndexed("hello") -> h4e3l2l1o0
     */
   public static void printIndexed(String s) {
    String ret = "";
    for (int i = s.length() - 1; i >= 0; i--){
      ret += s.charAt(s.length() - 1 - i);
      ret += i;
    }
    System.out.println(ret);
   }

   public static void main(String[] args) {
      printIndexed("hello");
      printIndexed("cat"); // should print c2a1t0
   }
}