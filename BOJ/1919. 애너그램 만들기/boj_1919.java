/*
두 문자열 각각에서 일부 문자를 제거하면, 두 문자열이 애너그램 관계에 있을 수 있다.
각 문자열에 대해 알파벳 26개만큼의 크기를 가지는 int형 1차원 배열을 생성하고, 문자의 개수를 센다.
그 후 26회만큼의 for loop를 통해 두 배열에서의 값의 절댓값 차를 구한다!
값이 동일하다면, 같은 횟수만큼의 문자가 두 문자열 각각에 포함되어있다는 것이고, 순서를 바꾸면 같은 문자가 되는 애너그램 관계에 해당하기 때문이다.
 */

import java.io.*;
import java.lang.Math;

public class boj_1919 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String firstWord = br.readLine();
        String secondWord = br.readLine();
        int[] arr1 = new int[27];
        int[] arr2 = new int[27];
        int count = 0;

        for (int i = 0; i < firstWord.length(); i++) {
            arr1[firstWord.charAt(i) - 'a']++;    // 이렇게 해주자! ...charAt(i) - 97 처럼 직접 값을 넣지는 말자.
        }

        for (int j = 0; j < secondWord.length(); j++) {
            arr2[secondWord.charAt(j) - 'a']++;
        }

        for (int l = 0; l < 27; l++) {
            count += Math.abs(arr1[l] - arr2[l]);
        }

        System.out.println(count);
    }
}
