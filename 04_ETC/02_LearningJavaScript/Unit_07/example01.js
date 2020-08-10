const x = 3;

function f() {
  console.log(x);
  console.log(y);
}

{
  const y = 5;
  f();
}
