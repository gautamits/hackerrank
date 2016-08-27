import java.io.*;
import java.util.*;

public class Solution {
static boolean isAnagram(String a, String b) {
    boolean ret = true ;
    a=a.toUpperCase();
    b=b.toUpperCase();
    Map<Character,Integer> map1 = new HashMap<Character,Integer>();
    Map<Character,Integer> map2 = new HashMap<Character,Integer>();
    for(int i = 0; i < a.length(); i++){
       char c = a.charAt(i);
       Integer val = map1.get(new Character(c));
       if(val != null){
         map1.put(c, new Integer(val + 1));
       }
        else{
         map1.put(c,1);
       }
    }
    for(int i = 0; i < b.length(); i++){
       char c = b.charAt(i);
       Integer val = map2.get(new Character(c));
       if(val != null){
         map2.put(c, new Integer(val + 1));
       }else{
         map2.put(c,1);
       }
    }

    // Complete the function by writing your code here.
    if(map1.size()!=map2.size()) return false;
    for (final Character key : map1.keySet()) {
        if (map2.containsKey(key)) {
            int t1=map1.get(key);
            int t2=map2.get(key);
            if(t1!=t2)
                return false;
        }
        else return false;
    }
    return ret;

}
public static void main(String[] args) {

    Scanner scan = new Scanner(System.in);
    String a = scan.next();
    String b = scan.next();
    scan.close();
    boolean ret = isAnagram(a, b);
    System.out.println( (ret) ? "Anagrams" : "Not Anagrams" );
}
}
