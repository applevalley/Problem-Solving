import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.lang.Math;

public class boj_2579 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int stairNumber = Integer.parseInt(br.readLine());
        int[] stairs = new int[stairNumber];
        int[] dp = new int[stairNumber + 1];

        for (int i = 0; i < stairNumber; i++) {
            int singleStair = Integer.parseInt(br.readLine());
            stairs[i] = singleStair;
        }

        dp[1] = stairs[0];

        if (stairNumber >= 2) {
            dp[2] = Math.max(stairs[0] + stairs[1], stairs[1]);

            if (stairNumber > 2) {

                for (int j = 3; j < stairNumber + 1; j++) {
                    dp[j] = Math.max(dp[j - 3] + stairs[j - 2] + stairs[j - 1], dp[j - 2] + stairs[j - 1]);
                }
            }
        }
        System.out.println(dp[stairNumber]);
    }
}
