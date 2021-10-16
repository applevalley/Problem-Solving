import java.util.*;
import java.io.*;

public class boj_10828 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        Stack<Integer> ms = new Stack<>();
        for(int i = 0; i < N; i++) {
            String order = br.readLine();
            if(order.contains("push")) {
                String[] number = order.split(" ");
                ms.add(Integer.parseInt(number[1]));
            } else if(order.contains("pop")) {
                if (ms.isEmpty()) {
                    System.out.println(-1);
                } else {
                  System.out.println(ms.pop());
                }
            } else if(order.contains("size")) {
                System.out.println(ms.size());
            } else if(order.contains("empty")) {
                if(ms.isEmpty()) {
                    System.out.println(1);
                } else {
                    System.out.println(0);
                }
            } else {
                if(ms.isEmpty()) {
                    System.out.println(-1);
                } else {
                    System.out.println(ms.peek());
                }
            }
        }
    }
}
