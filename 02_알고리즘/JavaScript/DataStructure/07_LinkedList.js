/* (단방향) 연결리스트 */
function LinkedList() {
  let length = 0;
  let head = null;

  let Node = function (element) {
    this.element = element;
    this.next = null;
  };

  this.size = function () {
    return length;
  };
  this.head = function () {
    return head;
  };

  // print함수는 해당 강의에는 없는데 링크드 리스트로 잘 구현됬는지
  // 확인차원에서 배옇형태로 만들어서 출력해보고자 구현함.
  this.print = function () {
    let currentNode = head;
    let arr = [];
    while (currentNode) {
      arr.push(currentNode.element);
      currentNode = currentNode.next;
    }
    return arr;
  };

  this.add = function (element) {
    let node = new Node(element);
    if (head === null) {
      head = node;
    } else {
      let currentNode = head;
      //next가 null이면 맨 마지막 노드
      while (currentNode.next) {
        currentNode = currentNode.next;
      }
      currentNode.next = node;
    }
    length++;
  };

  //삭제시, 찾는요소가 head에 있을경우와, 맨끝 혹은 시작과끝사이에 있을 경우 나눠 생각
  this.remove = function (element) {
    let currentNode = head;
    let prevNode;
    //삭제할 값이 헤드의 요소와 일치하는 경우에는 head를 다음 노드로 수정
    if (currentNode.element === element) {
      head = currentNode.next;
    } else {
      //헤드에 찾는 요소가 없을경우, 일치하는 위치까지 이전노드와 현재노드를 업데이트해감
      while (currentNode.element !== element) {
        prevNode = currentNode;
        currentNode = currentNode.next;
      }
      //이전노드의 다음값을 현재노드의 다음값으로 설정함으로써, 찾던 요소는 연결리스트에서 제거됨
      prevNode.next = currentNode.next;
    }
    length--;
  };

  this.isEmpty = function () {
    return length === 0;
  };

  this.indexOf = function (element) {
    let currentNode = head;
    let idx = -1;
    //head부터 tail까지 반복해서 찾고자하는 요소와 일치하는 곳이 있다면, 해당 idx 반환
    while (currentNode) {
      idx++;
      if (currentNode.element === element) {
        return idx;
      }
      currentNode = currentNode.next;
    }
    //다 돌아봤는데 일치하는 값이 없으면, -1을 반환
    return -1;
  };

  //찾고자하는 index의 요소를 찾아주는 메서드
  this.elementAt = function (idx) {
    let currentNode = head;
    let cnt = -1;
    while (cnt < idx) {
      cnt++;
      currentNode = currentNode.next;
    }
    return currentNode.element;
  };

  //원하는 위치에 요소 추가하기
  this.addAt = function (idx, element) {
    let node = new Node(element);
    let currentNode = head;
    let prevNode;
    let currentIdx = 0;

    //찾는 위치가 링크드 리스트 밖에 있는경우 false반환
    if (idx > length) {
      return false;
    }
    //넣고자 하는 위치가 맨 앞일때
    if (idx === 0) {
      node.next = currentNode;
      head = node;
    } else {
      while (idx > currentIdx) {
        currentIdx++;
        prevNode = currentNode;
        currentNode = currentNode.next;
      }
      node.next = currentNode;
      prevNode.next = node;
    }
    length++;
  };

  this.removeAt = function (idx) {
    let currentNode = head;
    let prevNode;
    let currentIdx = 0;

    if (idx >= length || idx < 0) {
      return null;
    } else {
      while (idx > currentIdx) {
        currentIdx++;
        prevNode = currentNode;
        currentNode = currentNode.next;
      }
      prevNode.next = currentNode.next;
    }
    length--;
    return currentNode.element;
  };
}

let l = new LinkedList();
console.log(l.isEmpty());
l.add("1번");
l.add("2번");
l.add("3번");
l.add("4번");
l.add("5번");
l.add("6번");

console.log(l.print());
console.log(l.print());
console.log(l.remove("5번"));
console.log(l.print());
console.log(l.removeAt(2));
console.log(l.print());
console.log(l.addAt(2, "test"));
console.log(l.print());
console.log(l.indexOf("test"));
console.log(l.size());
