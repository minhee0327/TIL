interface Shape {
  getArea(): number;
}

class Circle implements Shape {
  //   radius: number;

  constructor(public radius: number) {
    this.radius = radius;
  }
  getArea() {
    return this.radius * this.radius * Math.PI;
  }
}

class Rectagle implements Shape {
  //   width: number;
  //   height: number;
  constructor(private width: number, private height: number) {
    this.width = width;
    this.height = height;
  }
  getArea() {
    return this.width * this.height;
  }
}

const circle = new Circle(5);
const rect = new Rectagle(5, 10);

console.log(circle.radius);
// console.log(rect.width); // private에 의해 외부에서 접근 불가

const shapes: Shape[] = [new Circle(5), new Rectagle(10, 5)];

shapes.forEach((shape) => {
  console.log(shape.getArea());
});
