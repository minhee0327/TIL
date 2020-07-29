const obj = {};

obj.color = "yellow";

obj["not an identifier"] = 3;
console.log(obj["not an identifier"]);
console.log(obj["color"]);

const SIZE = Symbol();
obj[SIZE] = 8;
console.log(obj[SIZE]);
console.log(obj);

obj.SIZE = 0;
console.log(obj[SIZE]); //8
console.log(obj.SIZE); //0
console.log(obj["SIZE"]); //0

const now = new Date();
console.log(now);

const halloweenParty = new Date(2016, 9, 31, 19, 0); //2016-10-31 19:00
console.log(halloweenParty.getFullYear());
console.log(halloweenParty.getMonth());
console.log(halloweenParty.getUTCDate()); //...
