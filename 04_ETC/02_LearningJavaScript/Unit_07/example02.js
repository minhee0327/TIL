{
  let x = { color: "blue" };
  let y = x;
  let z = 3;
  {
    let x = 10; //바깥의 x는 가려짐
    console.log(x); // 10
    console.log(y); //blue // y가 가리키는 외부스코프의 x가 가리키는 객체는 스코프 내에도 있음

    y.color = "red";
    console.log(z); //3 // z는 숩겨지지 않음(내부 스코프에서 새로 z를 할당하지 않았기 때문)
  }
  console.log(x.color); // 'red' 객체는 내부 스코프에서 수정함
  console.log(y.color); // x와 y는 같은 객체를 가리키고 있기 때문에 동일하게 red임
  console.log(z);
}
