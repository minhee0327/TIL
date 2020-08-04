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
          return null;
        }
      };
    }
  }

  findMin() {
    let current = this.root;
    while (current.left !== null) {
      current = current.left;
    }
    return current.data;
  }

  fimdMax() {
    let current = this.root;
    while (current.right !== null) {
      current = current.right;
    }
    return current;
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
        //왼쪽, 오른쪽 자식 모두 없을 경우
        if (node.left == null && node.right == null) {
          return null;
        }
        //오른쪽 자식이 있을 경우
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

  //is Balance부터 다시 봐야함.
}
