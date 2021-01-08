package day08_stack;

import java.util.Scanner;
import java.util.Stack;

public class Main10828_스택2 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		
		Stack<Integer> stack = new Stack<Integer>();
		
		for (int i = 0; i <= n; i++) {
			String instruction = sc.nextLine();
			if(instruction.contains("push")) {
				String [] s = instruction.split(" ");
				stack.add(Integer.parseInt(s[1]));
			}else if (instruction.contains("pop")) {
				if (stack.isEmpty()) {
					System.out.println(-1);
				}else {
					System.out.println(stack.pop());
				}
			}else if (instruction.contains("size")) {
				System.out.println(stack.size());
			}else if (instruction.contains("empty")) {
				if (stack.isEmpty()) {
					System.out.println(1);
				}else {
					System.out.println(0);
				}
			}else if (instruction.contains("top")) {
				if(stack.isEmpty()) {
					System.out.println(-1);
				}else {
					System.out.println(stack.peek());
				}
			}
		}
	}

}
