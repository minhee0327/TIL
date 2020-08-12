class Car {
  //this: 일종의 placeholder, 메서드를 호출한 인스턴스를 가리키는 목적
  constructor(make, mode) {
    this.make = make;
    this.mode = mode;
    this._userGears = ["P", "N", "R", "D"];
    //가짜접근제한
    //this._userGrear = this._userGrears[0];
  }
  get userGrear() {
    return this._userGear;
  }
  set userGrear(value) {
    if (this.userGears.indexOf(value) < 0)
      throw new Error(`Invalid gear:${value}`);
    this._userGear = value;
  }
  shift(gear) {
    this.userGear = gear;
  }
}

const car1 = new Car("Tesla", "Model 5");
const car2 = new Car("Mazda", "3i");

console.log(car1 instanceof Car); //true //car1은 Car의 instance
console.log(car1 instanceof Array); //false
console.log(car1 instanceof Object); //true

console.log(typeof car1);
