import java.io.*;

public class boj_2440 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        final int number = Integer.parseInt(br.readLine());

        for (int i = number; i > 0; i--) {
            for (int j = i; j > 0; j--) {
                sb.append("*");
            }
            for (int k = number - i; k > 0; k--) {
                sb.append(" ");
            }
            sb.append("\n");
        }
        System.out.println(sb);
    }
}
