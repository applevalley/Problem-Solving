import java.io.*;
public class boj_2445 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        final int number = Integer.parseInt(br.readLine());

        for (int i = 1; i <= number; i++) {
            for (int j = 1; j <= i; j++) {
                sb.append("*");
            }
            for (int k = 2 * (number - i); k > 0; k--) {
                sb.append(" ");
            }
            for (int l = 1; l <= i; l++) {
                sb.append("*");
            }
            sb.append("\n");
        }

        for (int i = number - 1; i > 0; i--) {
            for (int j = i; j > 0; j--) {
                sb.append("*");
            }
            for (int k = 2 * (number - i); k > 0; k--) {
                sb.append(" ");
            }
            for (int l = i; l > 0; l--) {
                sb.append("*");
            }
            sb.append("\n");
        }
        System.out.println(sb);
    }
}
