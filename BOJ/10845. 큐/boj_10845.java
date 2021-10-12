import java.util.*;

class Queue<T> {
    private ArrayList<T> queue= new ArrayList<>();

    public void push(T item) {
        queue.add(item);
    }

    public void pop() {
        if(queue.isEmpty()) {
            System.out.println(-1);
        }
        else {
            System.out.println(queue.remove(0));
        }

    }

    public void isEmpty() {
        if(queue.isEmpty()) {
            System.out.println(1);
        } else {
            System.out.println(0);
        }
    }

    public void size() {
        System.out.println(queue.size());
    }

    public void front() {
        if(queue.isEmpty()) {
            System.out.println(-1);
        } else {
            System.out.println(queue.get(0));
        }
    }

    public void back() {
        if(queue.isEmpty()) {
            System.out.println(-1);
        } else {
            System.out.println(queue.get(queue.size() - 1));
        }
    }

}

public class boj_10845 {

    public static void main(String[] args) {

        Queue<Integer> mq = new Queue<>();
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();

        for(int i = 0; i < N; i++) {
            String order = sc.next();
//            System.out.println(order);
            if(order.equals("push")) {
                int number = sc.nextInt();
                mq.push(number);
            } else if(order.equals("pop")) {
                mq.pop();
            } else if(order.equals("size")) {
                mq.size();
            } else if(order.equals("empty")) {
                mq.isEmpty();
            } else if(order.equals("front")) {
                mq.front();
            } else {
                mq.back();
            }

        }

    }
}
