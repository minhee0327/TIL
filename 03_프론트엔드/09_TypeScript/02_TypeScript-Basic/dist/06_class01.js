class Cart {
    constructor(user = user, store) {
        this.user = user;
        this.store = store;
    }
    put(temp) {
        this.store.id = temp.id;
    }
    get(id) {
        return this.store.id;
    }
}
class PromotionCart extends Cart {
    addPromotion() {
        this.user;
    }
}
let cart1 = new Cart({ name: 'john' }, { id: '1', price: 2000 });
let cart2 = new Cart({ name: 'jay' }, { id: '2', price: 3000 });
console.log(cart1);
console.log(cart2);
let cart3 = new PromotionCart({ name: 'mini' }, { id: '3', price: 1000 });
console.log(cart3);
//# sourceMappingURL=06_class01.js.map