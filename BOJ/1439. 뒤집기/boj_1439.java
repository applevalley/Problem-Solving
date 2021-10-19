import java.util.*;

public class boj_1439 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String myStr = sc.next();
        char[] count = myStr.toCharArray();

        int countZero = 0;
        int countOne = 0;
        boolean isZero = false;
        boolean isOne = false;

        for(char c: count) {
            if(c == '1') {
                if (!isOne) {
                    isOne = true;
                    isZero = false;
                    countOne++;
                }

            } else {
                if (!isZero) {
                    isZero = true;
                    isOne = false;
                    countZero++;
                }
            }
        }

        if (countOne < countZero) {
            System.out.println(countOne);
        } else {
            System.out.println(countZero);
        }
    }
}
