import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class boj_2439 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        final int number = Integer.parseInt(br.readLine());

        for (int i = 1; i < number + 1; i++) {
            for (int j = 1; j <= number - i; j++) {
                sb.append(" ");
            }
            for (int k = 1; k <= i; k++) {
                sb.append("*");
            }
            sb.append("\n");
        }
        System.out.println(sb);
    }
}
