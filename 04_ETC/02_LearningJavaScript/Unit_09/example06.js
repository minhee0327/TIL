class Vehicle {
  constructor() {
    this.passengers = [];
    console.log("Vehicle created!");
  }
  addPassenger(p) {
    this.passengers.push(p);
  }
}

//운송수단(vehicle)상속받음
class Car extends Vehicle {
  constructor() {
    //슈퍼클래스의 생성자 홏출
    super();
    console.log("Car created");
  }
  deployAirbags() {
    console.log("BWOOSH!");
  }
}

const v = new Vehicle();
v.addPassenger("Jamie");
v.addPassenger("Minhee");
console.log(v.passengers); //[ 'Jamie', 'Minhee' ]

const c = new Car();
c.addPassenger("Jonghuyn");
c.addPassenger("SangHee");
console.log(c.passengers); //[ 'Jonghuyn', 'SangHee' ]

console.log(c.deployAirbags());
// console.log(v.deployAirbags()); //undefined , is not a function
