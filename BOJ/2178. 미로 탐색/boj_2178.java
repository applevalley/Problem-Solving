import java.awt.*;
import java.util.*;
import java.io.*;

public class boj_2178 {
    static int[][] arr;
    static boolean[][] visit;
    static int n;
    static int m;
    static int[] dx = {-1, 1, 0, 0};
    static int[] dy = {0, 0, -1, 1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st1 = new StringTokenizer(br.readLine(), " ");

        n = Integer.parseInt(st1.nextToken());
        m = Integer.parseInt(st1.nextToken());

        arr = new int[n][m];
        visit = new boolean[n][m];

        for (int i = 0; i < n; i++) {
            String row = br.readLine();
            for (int j = 0; j < m; j++) {
                arr[i][j] = row.charAt(j) - '0';
            }
        }

        visit[0][0] = true;
        bfs(0, 0);
        System.out.println(arr[n - 1][m - 1]);

    }

    public static void bfs(int x, int y) {
        Queue<int[]> myQ = new LinkedList<>();
        myQ.add(new int[] {x, y});

        while (!myQ.isEmpty()) {
            int[] point = myQ.poll();
            int point_x = point[0];
            int point_y = point[1];

            for (int i = 0; i < 4; i++) {
                int tx = point_x + dx[i];
                int ty = point_y + dy[i];

                if (tx < 0 || ty < 0 || tx >= n || ty >= m) {
                    continue;
                }

                if (visit[tx][ty] || arr[tx][ty] == 0) {
                    continue;
                }

                myQ.add(new int[] {tx, ty});
                arr[tx][ty] = arr[point_x][point_y] + 1;
                visit[tx][ty] = true;
            }
        }
    }
}
