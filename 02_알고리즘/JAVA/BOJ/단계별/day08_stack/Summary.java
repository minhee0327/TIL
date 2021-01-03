package day08_stack;

public class Summary {

	public static void main(String[] args) {
//		1. java에서 제공하는 Stack class 활용하기
//		Stack <E> stack = new Stack<E>();
	
//		2. 기본 method
//		push(E item), peek(), empty(), search(Object o);
		
//		3. 직접 스택 구현해보기
//		3.1 배열로구현
		ArrayStack stack = new ArrayStack(10);
		System.out.println(stack.isEmpty());
		stack.push(2);
		stack.push(3);
		stack.push(4);
		System.out.println(stack.peek());
		System.out.println(stack.pop());
		System.out.println(stack.peek());
		System.out.println(stack.isEmpty());
		System.out.println("---");
		stack.printStack();
		
//		3.2 linked list로 구현(pass, 추후 collections리뷰마치고 다시 해보겠음;)
		
		
	}
}
