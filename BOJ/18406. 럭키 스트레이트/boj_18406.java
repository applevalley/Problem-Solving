import java.util.*;

public class boj_18406 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String points = sc.next();
        char[] divide = points.toCharArray();
        int left = 0;
        int right = 0;

        for(int i = 0; i < points.length(); i++) {
            if (i < (int)points.length() / 2) {
                left += divide[i];
            } else {
                right += divide[i];
            }
        }

        if (left == right) {
            System.out.println("LUCKY");
        } else {
            System.out.println("READY");
        }
    }
}
