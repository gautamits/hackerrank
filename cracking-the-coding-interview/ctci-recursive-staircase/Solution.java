import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int s = in.nextInt();
        
        for(int a0 = 0; a0 < s; a0++){
            int n = in.nextInt();
            int[] arr=new int[n+1];
            System.out.println(countWays(n,arr));
        }
    }
    public static int countWays(int n, int[] map) {

   if(n == 0 || n==1)
     return 1;
   if(n == 2)
     return 2;
   map[0] = 1;
   map[1] = 1;
   map[2] = 2;
   for (int i = 3; i <= n; i++) {

       //Problem with writing it this way: index could be negative
       map[i] = map[i - 1] + map[i - 2] + map[i - 3];

   }

return map[n];
    }
}