import java.util.*;
import java.io.*;

class Recursive1003 {
    int cntZero = 1;
    int cntOne = 0;
    int temp = 1;

    public int dp(int i) {
        if (i == 0) {
            return 0;
        } else if (i == 1) {
            cntZero = 0;
            cntOne = 1;
            return i;
        }

        Integer[] memoi = new Integer[i + 1];
        memoi[0] = 0;
        memoi[1] = 1;

        for (int x = 0; x < i; x++) {
            cntZero = cntOne;
            cntOne = temp;
            temp = cntZero + cntOne;
        }

        for (int x = 2; x < i + 1; x++) {
            memoi[x] = memoi[x - 1] + memoi[x - 2];
        }

        return memoi[i];
    }
}

public class boj_1003 {
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(bf.readLine());

        for (int tc = 0; tc < T; tc++) {
            Recursive1003 fibo = new Recursive1003();
            int n = Integer.parseInt(bf.readLine());
            fibo.dp(n);
            System.out.println(fibo.cntZero + " " + fibo.cntOne);
        }
    }
}
