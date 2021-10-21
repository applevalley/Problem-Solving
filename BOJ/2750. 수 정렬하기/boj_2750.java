import java.util.*;
import java.io.*;

public class boj_2750 {
    public static void main(String[] args) throws IOException {
        ArrayList<Integer> myList = new ArrayList<>();
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(bf.readLine());
        for (int i = 0; i < N; i++) {
            int number = Integer.parseInt(bf.readLine());
            myList.add(number);
        }

        for (int i = 0; i < myList.size() - 1; i++) {
            for (int j = 0; j < myList.size() - 1; j++) {
                if (myList.get(j) > myList.get(j + 1)) {
                    Collections.swap(myList, j, j + 1);
                }
            }
        }

        for (int i: myList) {
            System.out.println(i);
        }
    }
}
