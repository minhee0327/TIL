let MaxHeap = function () {
  let heap = [null];

  this.insert = function (num) {
    heap.push(num);
    if (heap.length > 2) {
      let idx = heap.length - 1;
      while (heap[idx] > heap[Math.floor(idx / 2)]) {
        if (idx >= 1) {
          [heap[Math.floor(idx / 2)], heap[idx]] = [
            heap[idx],
            heap[Math.floor(idx / 2)],
          ];
          if (Math.floor(idx / 2) > 1) {
            idx = Math.floor(idx / 2);
          } else {
            break;
          }
        }
      }
    }
  };

  this.remove = function () {
    //0은 null, 1부터 가장 작은값
    let biggest = heap[1];

    if (heap.length > 2) {
      heap[1] = heap[heap.length - 1];
      heap.splice(heap.length - 1);
      if (heap.length === 3) {
        if (heap[1] < heap[2]) {
          [heap[1], heap[2]] = [heap[2], heap[1]];
        }
        return biggest;
      }

      let i = 1;
      let left = i * 2;
      let right = i * 2 + 1;
      while (heap[i] <= heap[left] || heap[i] <= heap[right]) {
        if (heap[left] > heap[right]) {
          [heap[i], heap[left]] = [heap[left], heap[i]];
          i = i * 2;
        } else {
          [heap[i], heap[right]] = [heap[right], heap[i]];
          i = i * 2 + 1;
        }
        left = i * 2;
        right = i * 2 + 1;
        if (heap[left] == undefined || heap[right] === undefined) {
          break;
        }
      }
    } else if (heap.length === 2) {
      heap.splice(1, 1);
    } else {
      return null;
    }
    return biggest;
  };

  this.sort = function () {
    let result = new Array();
    while (heap.length > 1) {
      result.push(this.remove());
    }
    return result;
  };

  this.print = () => console.log(heap);
};

let mh = new MaxHeap();
mh.insert(1);
mh.print();
mh.insert(10);
mh.print();
mh.insert(2);
mh.print();
mh.insert(7);
mh.print();
mh.insert(3);
mh.print();
mh.remove(3);
mh.print();
console.log(mh.sort()); //최소값 순 배열
