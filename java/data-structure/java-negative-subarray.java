import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner in = new Scanner(System.in);
        int n=in.nextInt();
        int count=0;
        int[] arr = new int[n];
        for(int i=0;i<n;i++) arr[i]=in.nextInt();

        for(int i=0;i<n;i++){
            for(int j=1;j<arr.length-i+1;j++){
               if(Arrays.stream(Arrays.copyOfRange(arr,i,i+j)).sum()<0) count++;
            }
        }
        System.out.println(count);
    }
}
