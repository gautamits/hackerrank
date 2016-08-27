import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String s = scan.nextLine();
        scan.close();
        String[] words = s.split("[^A-Za-z]+");
		if (words.length > 0 && words[0].isEmpty()) {
			words = Arrays.copyOfRange(words, 1, words.length);
		}

		System.out.println(words.length);
		for (String word : words) {
			System.out.println(word);
		}
    }
}
