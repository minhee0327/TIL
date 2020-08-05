/*
[BST Class 구현함수]
- add(), findMin(), findMax(), find(Data), isPresent, remove(data), 
- findMinHeight, findMaxHeight, isBalanced;
- preOrder, InOrder, postOrder, levelOrder
*/
class Node {
  constructor(data, left = null, right = null) {
    this.data = data;
    this.left = left;
    this.right = right;
  }
}

class BST {
  constructor() {
    this.root = null;
  }

  //data 넣기
  add(data) {
    const node = this.root;
    //아직 트리가 비어있으면 새로 들어온 데이터를 넣어주고 끝.
    if (node === null) {
      this.root = new Node(data);
      return;
    } else {
      const searchTree = function (node) {
        if (data < node.data) {
          if (node.left === null) {
            node.left = new Node(data);
            return;
          } else if (node.left !== null) {
            return searchTree(node.left);
          }
        } else if (data > node.data) {
          if (node.right === null) {
            node.right = new Node(data);
            return;
          } else if (node.right !== null) {
            return searchTree(node.right);
          }
        } else {
          //이진트리에 equal값이 들어오면 넣을 필요가 없음
          return null;
        }
      };
      return searchTree(node);
    }
  }

  findMin() {
    let current = this.root;
    //null이 아니라면 계속 작은 값이 있다는 이야기, left로 이동.
    while (current.left !== null) {
      current = current.left;
    }
    //current는 마지막 left node를 가짐
    return current.data;
  }

  findMax() {
    let current = this.root;
    while (current.right !== null) {
      current = current.right;
    }
    return current.data;
  }
  //data유무 체크 (있을경우 해당 데이터 반환, 없을경우 null반환)
  find(data) {
    let current = this.root;
    while (data !== current.data) {
      if (data < current.data) {
        current = current.left;
      } else {
        current = current.right;
      }
      if (current === null) {
        return null;
      }
    }
    return current;
  }
  //존재 유무 체크(있을경우 true, 없을 경우 false반환)
  isPresent(data) {
    let current = this.root;
    while (current) {
      if (data === current.data) {
        return true;
      }
      if (data < current.data) {
        current = current.left;
      } else {
        current = current.right;
      }
    }
    return false;
  }

  remove(data) {
    const removeNode = function (node, data) {
      if (node == null) {
        return null;
      }
      if (data == node.data) {
        //자식노드 유무 체크
        //왼쪽, 오른쪽 자식 모두 없을 경우  //해당 노드를 null로 만들어서 삭제
        if (node.left == null && node.right == null) {
          return null;
        }
        //오른쪽 자식이 있을 경우 //해당노드를 오른쪽자식노드로 바꿈
        if (node.left === null) {
          return node.right;
        }
        //왼쪽 자식이 있을 경우
        if (node.right === null) {
          return node.left;
        }
        //둘다 자식이 있는 경우
        let tempNode = node.right;
        while (tempNode.left != null) {
          tempNode = tempNode.left;
        }
        node.data = tempNode.data;
        node.right = removeNode(node.right, tempNode.data);
        return node;
      } else if (data < node.data) {
        node.left = removeNode(node.left, data);
        return node;
      } else if (data > node.data) {
        node.right = removeNode(node.right, data);
        return node;
      }
    };
    this.root = removeNode(this.root, data);
  }

  //루트 노드 ~ 두 자식(좌,우)을 가지지 않는 노드까지의 거리
  findMinHeight(node = this.root) {
    if (node == null) {
      return -1;
    }
    let left = this.findMinHeight(node.left);
    let right = this.findMinHeight(node.right);
    if (left < right) {
      return left + 1;
    } else {
      return right + 1;
    }
  }

  //루트 ~ 최대높이
  findMaxHeight(node = this.root) {
    if (node == null) {
      return -1;
    }
    let left = this.findMaxHeight(node.left);
    let right = this.findMaxHeight(node.right);
    if (left < right) {
      return right + 1;
    } else {
      return left + 1;
    }
  }

  //두 거리차이가 0 또는 1일때 searching시 O(logN)에 가깝기 때문에 체크
  //최대 거리와 최소거리차가 0이거나 1일 경우, 가장 균형잡힌 트리에 가깝다.
  isBalanced() {
    return this.findMinHeight() >= this.findMaxHeight() - 1;
  }

  //전위순회 (root - left - right)
  preOrder() {
    if (this.root == null) {
      return null;
    } else {
      let result = new Array();
      function traversePreOrder(node) {
        result.push(node.data);
        node.left && traversePreOrder(node.left);
        node.right && traversePreOrder(node.right);
      }
      traversePreOrder(this.root);
      return result;
    }
  }
  //중위 순회 (left - root - right)
  inOrder() {
    if (this.root == null) {
      return null;
    } else {
      let result = new Array();
      const traverseInIOrder = (node) => {
        node.left && traverseInIOrder(node.left);
        result.push(node.data);
        node.right && traverseInIOrder(node.right);
      };
      traverseInIOrder(this.root);
      return result;
    }
  }
  //후위순회 (left - right - root)
  postOrder() {
    if (this.root == null) {
      return null;
    } else {
      let result = new Array();
      function traversePostOrder(node) {
        node.left && traversePostOrder(node.left);
        node.right && traversePostOrder(node.right);
        result.push(node.data);
      }
      traversePostOrder(this.root);
      return result;
    }
  }

  //레벨순회 [BFS처럼 구현]
  levelOrder() {
    let result = [];
    let Q = [];

    if (this.root != null) {
      Q.push(this.root);
      while (Q.length > 0) {
        let node = Q.shift();
        result.push(node.data);
        if (node.left != null) {
          Q.push(node.left);
        }
        if (node.right != null) {
          Q.push(node.right);
        }
      }
      return result;
    } else {
      return null;
    }
  }
}

let b = new BST();
b.add(4);
b.add(2);
b.add(6);
b.add(1);
b.add(3);
b.add(5);
b.add(7);

b.remove(4);
console.log(b.findMin());
console.log(b.findMax());
b.remove(7);
console.log(b.findMax());
console.log(b.isPresent(4));

console.log("-----------순회--------");

let bst = new BST();

bst.add(9);
bst.add(4);
bst.add(17);
bst.add(3);
bst.add(6);
bst.add(22);
bst.add(5);
bst.add(7);
bst.add(20);

console.log(bst.findMinHeight());
console.log(bst.findMaxHeight());
console.log(bst.isBalanced());

bst.add(10);
console.log(bst.findMinHeight());
console.log(bst.findMaxHeight());
console.log(bst.isBalanced());

console.log("inOrder: " + bst.inOrder());
console.log("preOrder: " + bst.preOrder());
console.log("postOrder: " + bst.postOrder());
console.log("levelOrder: " + bst.levelOrder());
