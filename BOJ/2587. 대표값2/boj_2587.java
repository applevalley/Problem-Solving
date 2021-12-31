import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;

public class boj_2587 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        ArrayList<Integer> arr = new ArrayList<>();
        int totalValue = 0;

        for (int i = 0; i < 5; i++) {
            int singleNumber = Integer.parseInt(br.readLine());
            arr.add(singleNumber);
            totalValue += singleNumber;
        }

        Collections.sort(arr);
        System.out.println((int)totalValue / 5 + "\n" + arr.get(2));
    }
}
