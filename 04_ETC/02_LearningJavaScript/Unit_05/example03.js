/*
//무한 루프에 빠지게됨. 
//0.1 은 이진 표현으로 나타낼 수 있는 숫자 사이에 걸쳐있기 때문에, 0.3을 살짝 벗어나서 0.30000000000000004 와 0.3을 비교함.
//따라서 0.3을 넘어선 값으로 무한 루프에 빠지게 됨.

let n = 0;
while (true) {
  n += 0.1;
  if (n === 0.3) break;
}

console.log(`Stopped at ${n}`);
*/

let n = 0;
while (true) {
  n += 0.1;
  if (Math.abs(n - 0.3) < Number.EPSILON) break;
}

console.log(`Stopped at ${n}`);
