/*
const o = {
  name: "MinHee",
  greetBackwards: function () {
    function getReverseName() {
      let nameBackwards = "";
      for (let i = this.name.length - 1; i >= 0; i--) {
        nameBackwards += this.name[i];
      }
      return nameBackwards;
    }
    return `${getReverseName()} si eman ym, olleH`;
  },
};
console.log(o.greetBackwards());
*/

// 객체 내부에서 사용한 this가 처음 호출한 시점에는 o에 연결이 되지만
// getBackwards 내부에서 getReverseName을 호출하면서, this는 o가 아닌 다른 것에 묶임
// 따라서 o객체의 this.name을 사용하고 싶다면 메서드 내에서 this를 변수에 할당해주어 사용해야함.(아래)

const o = {
  name: "Minhee",
  greetBackwards: function () {
    const self = this;
    function getReverseName() {
      let nameBackwards = "";
      for (let i = self.name.length - 1; i >= 0; i--) {
        nameBackwards += self.name[i];
      }
      return nameBackwards;
    }
    return ` ${getReverseName()} si eman yM, olleH`;
  },
};

console.log(o.greetBackwards());
