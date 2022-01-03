import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class boj_10093 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        long firstNumber = Long.parseLong(st.nextToken());
        long secondNnumber = Long.parseLong(st.nextToken());

        if (firstNumber == secondNnumber) {
            System.out.println(0);
        } else {
            if (firstNumber > secondNnumber) {
                long temp = firstNumber;
                firstNumber = secondNnumber;
                secondNnumber = temp;
            }
            StringBuilder sb = new StringBuilder();
            int cnt = 0;

            while (++firstNumber < secondNnumber) {
                sb.append(firstNumber).append(" ");
                cnt++;;
            }

            System.out.println(cnt + "\n" + sb.toString());
        }
    }
}
