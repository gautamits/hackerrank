import java.util.*;
import java.io.*;

class Solution{
    public static void main(String []argh){
        Scanner in = new Scanner(System.in);
        int t=in.nextInt();
        for(int i=0;i<t;i++){
            int a = in.nextInt();
            int b = in.nextInt();
            int n = in.nextInt();
            int sum=0;
            for(int i=0; i < n ;i++ ){
              sum=sum+(int)Math.pow(2,i)*b;
              System.out.print(a+sum+" ");
        }
        System.out.println("");
      }
        in.close();
    }
}
