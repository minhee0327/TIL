class Super {
  constructor() {
    this.name = "Super";
    this.isSuper = true;
  }
}

//가능하지만 비추
Super.prototype.sneaky = "not recommended!";

class Sub extends Super {
  constructor() {
    super();
    this.name = "Sub";
    this.isSub = true;
  }
}

const obj = new Sub();

for (let i in obj) {
  console.log(`${i}:${obj[i]}` + (obj.hasOwnProperty(i) ? "" : " (inherited)"));
}
