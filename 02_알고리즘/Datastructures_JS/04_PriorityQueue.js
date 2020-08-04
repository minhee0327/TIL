function PriorityQueue() {
  let collections = [];

  this.print = function () {
    console.log(collections);
  };

  this.enqueue = function (data) {
    if (this.isEmpty()) {
      collections.push(data);
    } else {
      let added = false;
      for (let i = 0; i < collections.length; i++) {
        if (data[1] < collections[i][1]) {
          collections.splice(i, 0, data);
          added = true;
          break;
        }
      }
      //만약 추가가 안됬으면 우선순위가 가장 낮으니까 마지막에 넣어주기
      if (!added) {
        collections.push(data);
      }
    }
  };

  this.dequeue = function () {
    return collections.shift()[0];
  };
  this.front = function () {
    return collections[0];
  };
  this.size = function () {
    return collections.length;
  };
  this.isEmpty = function () {
    return collections.length ? false : true;
  };
}

let pq = new PriorityQueue();
pq.enqueue(["Minhee", 2]);
pq.enqueue(["Jihye", 3]);
pq.enqueue(["Jonhyun", 1]);
pq.enqueue(["MinGuk", 2]);

pq.print();
pq.dequeue();
pq.print();
console.log(pq.front());
