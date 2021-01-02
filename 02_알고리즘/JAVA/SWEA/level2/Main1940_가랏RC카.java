package level2;

import java.util.Scanner;

public class Main1940_가랏RC카 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int T = sc.nextInt();
		for(int t = 0; t < T; t++) {
			int n = sc.nextInt();
			sc.nextLine();

			int currentSpeed = 0;
			int currentDistance = 0;
			
			for(int i = 0; i < n; i++) {
				String instruction = sc.nextLine();
				int command = instruction.charAt(0);
				if(command == '1') {
					currentSpeed += Integer.parseInt(String.valueOf(instruction.charAt(2)));
				}else if(command == '2') {
					int decreaseSpeed = Integer.parseInt(String.valueOf(instruction.charAt(2)));
					if(decreaseSpeed > currentSpeed) {
						currentSpeed = 0;
					}else {
						currentSpeed -= Integer.parseInt(String.valueOf(instruction.charAt(2)));
					}
				}
				currentDistance += currentSpeed;
			}
			
			System.out.printf("#%d %d%n", t+1, currentDistance);
		}
	}

}
