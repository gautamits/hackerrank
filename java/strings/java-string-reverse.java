import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {

        Scanner sc=new Scanner(System.in);
        String A=sc.next();
        StringBuilder builder = new StringBuilder();
        builder.append(A);
        builder = builder.reverse();
        if(A.compareTo(builder.toString())==0) System.out.println("Yes");
        else System.out.println("No");
        /* Enter your code here. Print output to STDOUT. */

    }
}
