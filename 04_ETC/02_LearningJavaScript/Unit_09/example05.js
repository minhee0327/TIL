class Car {
  static getNextVin() {
    //this.nextVin으로 써도 괜찮지만, Car를 앞에써서 정적 메서드점 상기하기 쉬워짐
    return Car.nextVin++;
  }

  constructor(make, mode) {
    this.make = make;
    this.mode = mode;
    this.vin = Car.getNextVin();
  }

  static areSimilar(car1, car2) {
    return car1.make === car2.make && car1.mode === car2.mode;
  }
  static areSame(car1, car2) {
    return car1.vin === car2.vin;
  }
}

Car.nextVin = 0;

const car1 = new Car("Tesla", "5");
const car2 = new Car("Hyundae", "3");
const car3 = new Car("Hyundae", "3");

console.log(car1.vin); //0
console.log(car2.vin); //1
console.log(car3.vin); //2

console.log(Car.areSimilar(car1, car2)); //false
console.log(Car.areSimilar(car2, car3)); //true
console.log(Car.areSame(car2, car3)); //false
console.log(Car.areSame(car2, car2)); //true
