import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.lang.Math.*;

public class boj_1475 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int[] plastic = new int[10];
        int minValue = 0;
        int roomNumber = Integer.parseInt(br.readLine());

        while (roomNumber > 0) {
            int dividedNumber = roomNumber % 10;
            if (dividedNumber == 6 || dividedNumber == 9) {
                if (plastic[6] <= plastic[9]) {
                    plastic[6] += 1;
                } else {
                    plastic[9] += 1;
                }
            } else {
                plastic[dividedNumber] += 1;
            }
            roomNumber /= 10;
        }

        for (int i = 0; i < 10; i++) {
            if (plastic[i] > minValue) {
                minValue = plastic[i];
            }
        }

        System.out.println(minValue);
    }
}