const Car = (function () {
  const carProps = new WeakMap();

  class Car {
    constructor(make, mode) {
      this.make = make;
      this.mode = mode;
      this._userGears = ["P", "N", "R", "D"];
      carProps.set(this, { userGear: this._userGears[0] });
    }
    get userGrear() {
      return carProps.get(this).userGear;
    }
    set userGear(value) {
      if (this.userGears.indexOf(value) < 0)
        throw new Error(`Invalid gear:${value}`);
      carProps.get(this).userGear = value;
    }
    shift(gear) {
      this.userGear = gear;
    }
  }
  return Car;
})();
