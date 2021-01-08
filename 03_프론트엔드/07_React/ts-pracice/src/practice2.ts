interface Person {
  name: string;
  age?: number; //?뜻 : 설정 해도 되고, 안해도 되는값
}

interface Developer extends Person {
  skills: string[];
}

const person: Person = {
  name: "민희",
  age: 30,
};

const expert: Developer = {
  name: "미니미",
  skills: ["js", "react"],
};

const people: Person[] = [person, expert];

//type 키워드로 타입정의하기
type Color = "red" | "orange" | "yellow";
const color: Color = "red";
const colors: Color[] = ["red", "orange"];
