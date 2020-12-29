function solution(n) {
  return "수박".repeat(n / 2) + (n % 2 ? "수" : "");
}

/**
 * 또는, repeat을 해서 '수박수박수박...'중에서 n의 길이만큼 slice하는 방법도 좋다.
 * 
 function solution(n) {
   return "수박".repeat(n).slice(0,n);
  }

 * 삼항연산자를 활용한 코드도 많으니 javaScript사용할때는 좀 더 신경써보는 걸로 노력하자.
 */
