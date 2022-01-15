/*
BufferedReader/Writer를 사용하지 않으면 반드시 시간초과가 나는 문제였다...!
입력은 곧잘 BufferedReader를 사용하였지만 출력은 System.out.println을 자주 사용했는데,
가급적이면 출력도 BufferedWriter를 사용하는 습관을 들여야겠다. flush() 메서드를 반복문 루프마다 사용하지 않도록 유의!
마지막엔 close()도 호출해주자.
 */

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.IOException;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.Collections;

public class boj_11931 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int numberCount = Integer.parseInt(br.readLine());
        Integer[] arr = new Integer[numberCount];

        for (int i = 0; i < numberCount; i++) {
            arr[i] = Integer.parseInt(br.readLine());
        }

        Arrays.sort(arr, Collections.reverseOrder());

        for (Integer e: arr) {
            bw.write(e + "\n");
        }

        bw.flush();
        bw.close();
    }
}
