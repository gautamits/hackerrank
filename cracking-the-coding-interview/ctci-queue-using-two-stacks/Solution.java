import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;
class MyQueue<T>{
    Stack<T> inbox = new Stack<T>();
    Stack<T> outbox = new Stack<T>();
    void enqueue(T i){
        inbox.push(i);
    }
    T dequeue(){
        if(outbox.empty()){
            while(!inbox.empty()) outbox.push(inbox.pop());
        }
        return outbox.pop();
    }
    T peek(){
        if(outbox.empty()){
            while(!inbox.empty()) outbox.push(inbox.pop());
        }
        return outbox.peek();
    }
}
public class Solution {
    public static void main(String[] args) {
        MyQueue<Integer> queue = new MyQueue<Integer>();

        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();

        for (int i = 0; i < n; i++) {
            int operation = scan.nextInt();
            if (operation == 1) { // enqueue
              queue.enqueue(scan.nextInt());
            } else if (operation == 2) { // dequeue
              queue.dequeue();
            } else if (operation == 3) { // print/peek
              System.out.println(queue.peek());
            }
        }
        scan.close();
    }
}