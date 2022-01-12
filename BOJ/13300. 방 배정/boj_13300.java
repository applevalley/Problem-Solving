/*
굳이 StringTokenizer 인스턴스를 생성할 필요가 없다!
1 3과 같이 공백을 기준으로 나누어진 입력을 받을 때,
String[] arr = br.readLine().split(" "); 처럼 String 데이터를 가지는 배열 형태로 선언한다.
그 후 int data = Integer.parseInt(arr[0]) 이렇게 바꾸어주면 된다!

그 외에도 우선 temp = br.readLine(); 처럼 선언하고,
temp.charAt(0) 처럼 해도 접근이 가능하다.
 */

import java.io.*;
import java.util.StringTokenizer;

public class boj_13300 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int[] man = new int[7];
        int[] woman = new int[7];
        int peopleCount = Integer.parseInt(st.nextToken());
        int peopleLimit = Integer.parseInt(st.nextToken());
        int roomCount = 0;

        for (int i = 0; i < peopleCount; i++) {
            StringTokenizer st2 = new StringTokenizer(br.readLine());
            int gender = Integer.parseInt(st2.nextToken());
            int grade = Integer.parseInt(st2.nextToken());

            if (gender == 0) {
                woman[grade]++;
            } else {
                man[grade]++;
            }
        }

        for (int j = 0; j < man.length; j++) {
            roomCount += Math.ceil(man[j] / (double)peopleLimit);
            roomCount += Math.ceil(woman[j] / (double)peopleLimit);
        }

        System.out.println(roomCount);
    }
}
