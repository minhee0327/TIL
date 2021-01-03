package day08_stack;

import java.util.Scanner;
import java.util.Stack;

public class Main10828_스택 {

	public static void main(String[] args) {
		//시간초과나서 수정 => StringBuffer로 출력 내용 담아서 출력함
		//bufferedReader, writer로 입출력받을까 했다가 변경.
		
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		
		Stack<Integer> stack = new Stack<Integer>();
		StringBuffer sb = new StringBuffer();
		
		for (int i = 0; i < n; i++) {
			String instruction = sc.next();
			if(instruction.equals("push")) {
				stack.add(sc.nextInt());
			}else if (instruction.equals("pop")) {
				if (stack.isEmpty()) {
					sb.append(-1 +"\n");
				}else {
					sb.append(stack.pop()+"\n");
				}
			}else if (instruction.equals("size")) {
				sb.append(stack.size()+"\n");
			}else if (instruction.equals("empty")) {
				if (stack.isEmpty()) {
					sb.append(1+"\n");
				}else {
					sb.append(0+"\n");
				}
			}else if (instruction.equals("top")) {
				if(stack.isEmpty()) {
					sb.append(-1+"\n");
				}else {
					sb.append(stack.peek()+"\n");
				}
			}
		}

		System.out.println(sb.toString());
	}
}
