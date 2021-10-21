import java.util.*;

public class boj_2752 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        ArrayList<Integer> myList = new ArrayList<>();

        for (int i = 0; i < 3; i++) {
            int number = sc.nextInt();
            myList.add(number);
        }

        for (int i = 0; i < myList.size() - 1; i++) {
            for (int j = 0; j < myList.size() - 1 - i; j++) {
                if (myList.get(j) > myList.get(j + 1)) {
                    Collections.swap(myList, j, j + 1);
                }
            }
        }


        for (int i: myList) {
            System.out.print(i + " ");
        }
    }
}