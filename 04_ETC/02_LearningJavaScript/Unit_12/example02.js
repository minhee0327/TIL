class Log {
  constructor() {
    this.messages = [];
  }
  add(message) {
    this.messages.push({ message, timestamp: Date.now() });
  }
  // 로그를 기록한 항목을 순회하고 싶을때 '이터러블 프로토콜'
  // Symbole.iterator가 있고, 이 메서드가 value와 done프로퍼티가 있는 객체를 반환하는 next 메서드를 가진 객체봔한하면
  // 해당 클래스의 인스턴스는 이터러블 객체라는 뜻을 가짐
  [Symbol.iterator]() {
    return this.messages.values();
  }
}

const log = new Log();
log.add("Learning JS");
log.add("JAVA");
log.add("nodeJS");

for (let entry of log) {
  console.log(`${entry.message}: ${entry.timestamp} `);
}

class Log2 {
  constructor() {
    this.messages = [];
  }
  add(message) {
    this.messages.push({ message, timestamp: Date.now() });
  }
  [Symbol.iterator]() {
    let i = 0;
    const messages = this.messages;
    return {
      next() {
        if (i >= messages.length) {
          return { value: undefined, done: true };
        }
        return { value: messages[i++], done: false };
      },
    };
  }
}
const log2 = new Log2();
log2.add("Learning JS");
log2.add("JAVA");
log2.add("nodeJS");

for (let entry of log2) {
  console.log(`${entry.message}: ${entry.timestamp}`);
}
