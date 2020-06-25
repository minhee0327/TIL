class Food {
    constructor(name) {
        this.name = name;
        this.brand = [];
    }
    addBrand(brand) {
        this.brand.push(brand);
    }
    print() {
        console.log(`${this.name} 를/을 파는 음식점들은`);
        console.log(this.brand.join(', '));
    }
}

const pizza = new Food('피자');
pizza.addBrand('임실');
pizza.addBrand('도미노');
pizza.print();

const chicken = new Food('치킨');
chicken.addBrand('굽네');
chicken.addBrand('푸라닭');
chicken.print();