function Queue() {
  collection = [];
  this.print = function () {
    console.log(collection);
  };
  this.enqueue = function (data) {
    collection.push(data);
  };
  this.dequeue = function () {
    return collection.shift();
  };
  this.front = function () {
    return collection[0];
  };
  this.size = function () {
    return collection.length;
  };
  this.isEmpty = function () {
    return collection.length ? false : true;
  };
}

let q = new Queue();
q.enqueue("A");
q.enqueue("B");
q.enqueue("C");
q.print();
q.dequeue();
q.print();
console.log(q.front());
