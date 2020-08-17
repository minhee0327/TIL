function a() {
  console.log("a: calling b");
  b();
  console.log("a: done");
}

function b() {
  console.log("a: calling c");
  c();
  console.log("b: done");
}

function c() {
  console.log("c: throwing error");
  throw new Error("c error");
  console.log("c: done");
}

function d() {
  console.log("d: calling c");
  c();
  console.log("d:done");
}

try {
  a();
} catch (e) {
  console.log(e.stack);
}

try {
  d();
} catch (e) {
  console.log(e.stack);
}

/*
//firefox에서 확인해보면 아래와 같은 결과 확인
//@이 의미하는 것이 스택 추적 맨 마지막엔 브라우저 자체를 가리키고 끝남

a: calling b 
a: calling c 
c: throwing error 
c@debugger eval code:15:9
b@debugger eval code:9:3
a@debugger eval code:3:3
@debugger eval code:26:3
debugger eval code:28:11

d: calling c debugger eval code:20:11
c: throwing error debugger eval code:14:11
c@debugger eval code:15:9
d@debugger eval code:21:3
@debugger eval code:32:3


*/
