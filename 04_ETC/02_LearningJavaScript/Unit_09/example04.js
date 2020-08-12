class Car {
  constructor(make, mode) {
    this.make = make;
    this.mode = mode;
    this.userGears = ["P", "N", "R", "D"];
    this.userGear = this.userGears[0];
  }

  shift(gear) {
    if (this.userGears.indexOf(gear) < 0)
      throw new Error(`Invalid gear:${gear}`);
    this.userGear = gear;
  }
}

const car1 = new Car();
const car2 = new Car();
console.log(car1.shift === Car.prototype.shift); //true
car1.shift("D");
// car1.shift("d"); // error: userGears에 d가 없음
console.log(car1.userGear); //'D'
console.log(car1.shift === car2.shift); //true

car1.shift = function (gear) {
  this.userGear = gear.toUpperCase();
};
console.log(car1.shift === Car.prototype.shift); //false
console.log(car1.shift === car2.shift); //false
car1.shift("d");
console.log(car1.userGear); //'D'
