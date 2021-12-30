import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class boj_10871 {
    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        StringBuilder sb = new StringBuilder();
        int maxValue = Integer.parseInt(st.nextToken());
        int targetValue = Integer.parseInt(st.nextToken());

        StringTokenizer st2 = new StringTokenizer(br.readLine());
        for (int i = 0; i < maxValue; i++) {
            int singleNumber = Integer.parseInt(st2.nextToken());
            if (singleNumber < targetValue) {
                sb.append(singleNumber).append(" ");
            }
        }
        System.out.println(sb.toString());
    }
}
