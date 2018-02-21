import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int N = in.nextInt();
        int sum = 0;
        int count = 0;

        for(int i=0; i < N; i++){
            sum += in.nextInt();
            
            if (sum % 2 == 1) {
                count += 2;
            }
        }

        System.out.println(sum % 2 == 0 ? count : "NO");
        
    }
}

