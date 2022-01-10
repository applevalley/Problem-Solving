import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class boj_2577 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int[] numberCount = new int[10];
        int firstNumber = Integer.parseInt(br.readLine());
        int secondNumber = Integer.parseInt(br.readLine());
        int thirdNumber = Integer.parseInt(br.readLine());
        int multipliedNumber = (firstNumber * secondNumber * thirdNumber);

        while (multipliedNumber > 0) {
            int dividedNumber = multipliedNumber % 10;
            numberCount[dividedNumber] += 1;
            multipliedNumber /= 10;
        }

        for (int e: numberCount) {
            System.out.println(e);
        }
    }
}