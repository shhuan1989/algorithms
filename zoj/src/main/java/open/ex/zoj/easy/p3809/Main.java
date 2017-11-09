package open.ex.zoj.easy.p3809;

/*
 * 
 * 
 * As an artist, Bob usually need to travel around the world. 
 * He made a lot of sketch of scenery on his journey. 
 * A famous spot he have visited recently is the Himalayas. 
 * The Himalayas is a mountain range in South Asia separating 
 * the plains of the Indian subcontinent from the Qinghai-Tibet 
 * Plateau. The Himalayas include over a hundred mountains 
 * exceeding 7,200 meters in elevation.

 One day, Bob came up with an strange idea. He wanted to know 
 the number of mountain peaks in his paintings. As his best friend, 
 he turned to you for help. You are given a list of N height sampling
 values Hi. You should determine how many peaks are there. For all i 
 which satisfies 2 <= i <= N - 1, Hi is defined as a peak if and only if Hi-1 < Hi > Hi+1.

 Input

 There are multiple test cases. The first line of input 
 contains an integer T indicating the number of test cases. For each test case:

 The first line contains one integer N (1 <= N <= 50). 
 The next line contains N integers Hi (1 <= Hi <= 8844). 
 It is guaranteed that any two adjacent height sampling values will be different.

 Output

 For each test case, output the number of peaks.

 Sample Input

 2
 9
 1 3 2 4 6 3 2 3 1
 5
 1 2 3 4 5
 Sample Output

 3
 0


 * 
 */

import java.util.Scanner;

public class Main {

	public static int CASE_COUNT;
	public static int N;
	public static final int MAX_N = 50;
	public static int[] HEIGHTS = new int[MAX_N];

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		CASE_COUNT = sc.nextInt();
		for(int i=0; i<CASE_COUNT; i++){
			N = sc.nextInt();
			for(int j=0; j<N; j++){
				HEIGHTS[j] = sc.nextInt();
			}
			System.out.println(countPeak());
		}
		sc.close();

	}
	
	public static int countPeak(){
		int c = 0;
		for(int i=1; i<N-1; i++){
			if(HEIGHTS[i]>HEIGHTS[i-1] && HEIGHTS[i]>HEIGHTS[i+1]){
				c++;
			}
		}
		return c;
	}

}
