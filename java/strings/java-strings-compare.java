import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        String str = in.next();
        int n = in.nextInt();
        String min=str.substring(0,n);
        String max=str.substring(0,n);
        String temp;
        for(int i=1;i<=str.length()-n;i++){
            temp=str.substring(i,i+n);
            //System.out.println(temp);
            if(temp.compareTo(min)<0) min=temp;
            if(temp.compareTo(max)>0) max=temp;
        }
        System.out.println(min);
        System.out.println(max);
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
    }
}
