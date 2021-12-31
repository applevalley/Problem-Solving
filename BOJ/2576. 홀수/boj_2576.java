import java.io.BufferedReader;
import java.io.InputStreamReader;

public class boj_2576 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int totalOddValue = 0;
        int minimumOddValue = 0xffffff;

        for (int i = 0; i < 7; i++) {
            int newNumber = Integer.parseInt(br.readLine());
            if (newNumber % 2 == 1) {
                if (minimumOddValue > newNumber) {
                    minimumOddValue = newNumber;
                }

                totalOddValue += newNumber;
            }
        }

        if (totalOddValue == 0) {
            System.out.println(-1);
        } else {
            System.out.println(totalOddValue + "\n" + minimumOddValue);
        }
    }
}