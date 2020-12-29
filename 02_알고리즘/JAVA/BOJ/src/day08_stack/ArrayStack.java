package day08_stack;

public class ArrayStack {
	int top;
	int [] stack;
	int size;
	//배열로 stack 구현 해 보기
	public ArrayStack(int size) {
		this.size = size;
		stack = new int [size];
		top = -1;
	};
	
	public boolean isEmpty() {
		return top == -1;
	}
	
	public boolean isFull() {
		return top == this.size -1;
	}
	
	public void push(int item) {
		if(isFull()) {
			System.out.println("스택 꽉 참");
		}else {
			stack[++top] = item;
		}
	}
	
	public int peek() {
		if(isEmpty()) {
			return -1;
		}else {
			return stack[top];
		}
		
	}

	public int pop() {
		if (isEmpty()) {
			return -1;
		}else {
			return stack[top--];
		}
	}
	
	public void printStack() {
		if(isEmpty()) {
			System.out.println("스택 비어있음..");
		}else {
			for (int i = 0; i <= top; i++) {
				System.out.println(stack[i]);
			}
		}
	}
	
	public void initializeStack() {
		if(isEmpty()) {
			System.out.println("이미 비어있음!");
		}else {
			top = -1;
			stack = new int[this.size];
			System.out.println("스택 초기화 완료!");
		}
	}

}
