import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;

public class boj_11328 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int testCase = Integer.parseInt(br.readLine());

        for (int i = 0; i < testCase; i++) {
            st = new StringTokenizer(br.readLine());
            int[] arr = new int[26];
            String first = st.nextToken();
            String second = st.nextToken();
            boolean checked = false;

            for (int j = 0; j < first.length(); j++) {
                int idx = (int)first.charAt(j) - 97;
                arr[idx]++;
            }

            for (int k = 0; k < second.length(); k++) {
                int idx = (int)second.charAt(k) - 97;
                arr[idx]--;
            }

            for (int e: arr) {
                if (e != 0) {
                    checked = true;
                    break;
                }
            }

            if (!checked) {
                System.out.println("Possible");
            } else {
                System.out.println("Impossible");
            }
        }
    }
}
