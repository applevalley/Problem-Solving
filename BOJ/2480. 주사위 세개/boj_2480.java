import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.math.*;

public class boj_2480 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int firstDice = Integer.parseInt(st.nextToken());
        int secondDice = Integer.parseInt(st.nextToken());
        int thirdDice = Integer.parseInt(st.nextToken());

        if (firstDice == secondDice && secondDice == thirdDice) {
            System.out.println(10000 + (firstDice * 1000));
        } else if (firstDice == secondDice && secondDice != thirdDice) {
            System.out.println(1000 + (firstDice * 100));
        } else if ((firstDice != secondDice && secondDice == thirdDice)) {
            System.out.println(1000 + (secondDice * 100));
        } else if ((firstDice == thirdDice && secondDice != thirdDice)) {
            System.out.println(1000 + (thirdDice * 100));
        } else {
            System.out.println(Math.max(Math.max(firstDice, secondDice), thirdDice) * 100);
        }
    }
}
