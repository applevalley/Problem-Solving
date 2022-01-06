import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class boj_10804 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int[] cards = new int[20];

        for (int i = 1; i < 21; i++) {
            cards[i - 1] = i;
        }

        for (int i = 0; i < 10; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int startPoint = Integer.parseInt(st.nextToken());
            int endPoint = Integer.parseInt(st.nextToken());

            for (int j = startPoint - 1; j < endPoint - 1; j++) {
                for (int k = j + 1; k < endPoint; k++) {
                    int temp = cards[k];
                    cards[k] = cards[j];
                    cards[j] = temp;
                }
            }
        }
        for (int l: cards) {
            System.out.print(l + " ");
        }
    }
}
