import java.util.*;

public class boj_1158 {
    public static void main(String[] args) {
        LinkedList<Integer> yose = new LinkedList<>();
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int K = sc.nextInt();
        StringBuilder eliminated = new StringBuilder();
        eliminated.append("<");

        for(int i = 1; i < N + 1; i++) {
            yose.add(i);
        }

        while(yose.size() > 1) {
            for(int i = 0; i < K - 1; i++) {
                yose.offer(yose.poll());
            }
            eliminated.append(yose.poll() + ", ");
        }

        eliminated.append(yose.poll() + ">");
        System.out.println(eliminated.toString());

    }
}

