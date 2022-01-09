import java.io.*;

public class boj_10808 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String word = br.readLine();
        int[] alpha = new int[26];

        for (int i = 0; i < word.length(); i++) {
            alpha[(int)word.charAt(i) - 97] += 1;
        }

        for (int e: alpha) {
            System.out.print(e + " ");
        }
    }
}
