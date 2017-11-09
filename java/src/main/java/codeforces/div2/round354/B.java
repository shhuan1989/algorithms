package codeforces.div2.round354;

import java.util.Scanner;

/**
 * Created by palad on 2016/5/26.
 *
 *
 * B. Pyramid of Glasses
 time limit per test1 second
 memory limit per test256 megabytes
 inputstandard input
 outputstandard output
 Mary has just graduated from one well-known University and is now attending celebration party. Students like to dream of a beautiful life, so they used champagne glasses to construct a small pyramid. The height of the pyramid is n. The top level consists of only 1 glass, that stands on 2 glasses on the second level (counting from the top), then 3 glasses on the third level and so on.The bottom level consists of n glasses.

 Vlad has seen in the movies many times how the champagne beautifully flows from top levels to bottom ones, filling all the glasses simultaneously. So he took a bottle and started to pour it in the glass located at the top of the pyramid.

 Each second, Vlad pours to the top glass the amount of champagne equal to the size of exactly one glass. If the glass is already full, but there is some champagne flowing in it, then it pours over the edge of the glass and is equally distributed over two glasses standing under. If the overflowed glass is at the bottom level, then the champagne pours on the table. For the purpose of this problem we consider that champagne is distributed among pyramid glasses immediately. Vlad is interested in the number of completely full glasses if he stops pouring champagne in t seconds.

 Pictures below illustrate the pyramid consisting of three levels.


 Input
 The only line of the input contains two integers n and t (1 ≤ n ≤ 10, 0 ≤ t ≤ 10 000) — the height of the pyramid and the number of seconds Vlad will be pouring champagne from the bottle.

 Output
 Print the single integer — the number of completely full glasses after t seconds.

 Examples
 input
 3 5
 output
 4
 input
 4 8
 output
 6
 Note
 In the first sample, the glasses full after 5 seconds are: the top glass, both glasses on the second level and the middle glass at the bottom level. Left and right glasses of the bottom level will be half-empty.
 */
public class B {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        int T = scanner.nextInt();

        int l = 1;
        int cups = 0;
        while (timeFullLevel(l) <= T) {
            l += 1;
        }

        l -= 1;
        cups = l * (l+1) / 2;
        T -= cups;

        if (T >= l) {
            cups += l-1;
        }
        cups = Math.min(cups, N*(N+1)/2);
        System.out.println(Math.max(0, cups));

    }

    public static int timeFullLevel(int level) {
        int result = 0;
        int t = 1;
        for (int i = 0; i < level; i++) {
            result += t;
            t *= 2;
        }
        return result;
    }
}
