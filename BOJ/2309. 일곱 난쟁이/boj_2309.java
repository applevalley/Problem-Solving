import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;


public class boj_2309 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        ArrayList<Integer> arr = new ArrayList<>();
        int totalValue = 0;
        int firstIdx = 0;
        int secondIdx = 0;

        for (int i = 0; i < 9; i++) {
            int singleNumber = Integer.parseInt(br.readLine());
            arr.add(singleNumber);
            totalValue += singleNumber;
        }

        int targetValue = totalValue - 100;

        outer: for (int i = 0; i < 8; i++) {
            for (int j = i + 1; j < 9; j++) {
                if (arr.get(i) + arr.get(j) == targetValue) {
                    firstIdx = i;
                    secondIdx = j;
                    break outer;
                }
            }
        }

        System.out.println(firstIdx + " " + secondIdx);
        arr.remove(arr.get(firstIdx));
        arr.remove(arr.get(secondIdx - 1));
        Collections.sort(arr);

        for (Integer e : arr) {
            System.out.println(e);
        }
    }
}
