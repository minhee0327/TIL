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
class InsurancePolicy {}
//고유한 심볼을 사용함으로서 믹스인이 다른 클래스와의 충돌 가능성을 낮춤
const ADD_POLICY = Symbol();
const GET_POLICY = Symbol();
const IS_INSURED = Symbol();
const _POLICY = Symbol();

function makeInsurable(o) {
  o[ADD_POLICY] = function (p) {
    this[_POLICY] = p;
  };
  o[GET_POLICY] = function () {
    return this[_POLICY];
  };
  o[IS_INSURED] = function () {
    return !!this[_POLICY];
  };
}

/*
function makeInsurable(o) {
  o.addInsurancePolicy = function (p) {
    this.InsurancePolicy = p;
  };
  o.getInsurancePolicy = function () {
    return this.InsurancePolicy;
  };
  o.isInsured = function () {
    return !!this.InsurancePolicy;
  };
  
}
*/

/* 
//가능한 방법이기는 한데 매번 makeInsurance를 호출해야함.
const car1 = new Car();
makeInsurable(car1)
car1.addInsurancePolicy(new InsurancePolicy());
*/

makeInsurable(Car.prototype);
const car1 = new Car();
car1.addInsurancePolicy(new InsurancePolicy());
