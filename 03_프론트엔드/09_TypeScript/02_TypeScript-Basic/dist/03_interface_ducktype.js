class Duck {
    sound() {
        console.log('꽥!');
    }
}
class Cat {
    sound() {
        console.log('야오옹');
    }
}
function makeSound(some) {
    some.sound();
}
makeSound(new Duck());
makeSound(new Cat());
//# sourceMappingURL=03_interface_ducktype.js.map