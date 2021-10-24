import java.util.*;
import java.io.*;

public class boj_11004 {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        ArrayList<Integer> myList = new ArrayList<>();
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());
        StringTokenizer st2 = new StringTokenizer(br.readLine());

        for (int i = 0; i < n; i++) {
            int number = Integer.parseInt(st2.nextToken());
            myList.add(number);
        }

        Collections.sort(myList);
        System.out.println(myList.get(k - 1));
        br.close();
    }
}
