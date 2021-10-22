import java.util.*;
import java.io.*;

public class boj_2751 {
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        ArrayList<Integer> myList = new ArrayList<>();
        int n = Integer.parseInt(bf.readLine());

        for (int i = 0; i < n; i++) {
            int number = Integer.parseInt(bf.readLine());
            myList.add(number);
        }

        Collections.sort(myList);

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < n; i++) {
            sb.append(myList.get(i) + "\n");
        }
        bw.write(sb.toString());
        bw.flush();
        bw.close();
        bf.close();
    }
}
