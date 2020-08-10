"use strict";
var Circle = /** @class */ (function () {
    //   radius: number;
    function Circle(radius) {
        this.radius = radius;
        this.radius = radius;
    }
    Circle.prototype.getArea = function () {
        return this.radius * this.radius * Math.PI;
    };
    return Circle;
}());
var Rectagle = /** @class */ (function () {
    //   width: number;
    //   height: number;
    function Rectagle(width, height) {
        this.width = width;
        this.height = height;
        this.width = width;
        this.height = height;
    }
    Rectagle.prototype.getArea = function () {
        return this.width * this.height;
    };
    return Rectagle;
}());
var circle = new Circle(5);
var rect = new Rectagle(5, 10);
console.log(circle.radius);
// console.log(rect.width); // private에 의해 외부에서 접근 불가
var shapes = [new Circle(5), new Rectagle(10, 5)];
shapes.forEach(function (shape) {
    console.log(shape.getArea());
});
