import java.util.*;
import java.io.*;

public class boj_1920 {
    public static int bs(ArrayList<Integer> targetList, int target) {
        int low = 0;
        int high = targetList.size() - 1;

        while (low <= high) {
            int mid = (low + high) / 2;

            if (target < targetList.get(mid)) {
                high = mid - 1;
            } else if (target > targetList.get(mid)) {
                low = mid + 1;
            } else {
                return 1;
            }
        }
        return 0;
    }
    public static void main(String[] args) throws IOException {
        ArrayList<Integer> myList = new ArrayList<>();
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());

        for (int i = 0; i < n; i++) {
            myList.add(Integer.parseInt(st.nextToken()));
        }
        Collections.sort(myList);

        int m = Integer.parseInt(br.readLine());
        StringTokenizer st2 = new StringTokenizer(br.readLine());
        for (int j = 0; j < m; j++) {
            int target = Integer.parseInt(st2.nextToken());
            System.out.println(bs(myList, target));
        }
    }
}
