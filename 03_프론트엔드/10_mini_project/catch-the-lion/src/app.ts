import HelloHi, { Hello, User } from './type';

const msg: Hello = {
    text: 'hello world',
};

console.log(msg.text, User.name);

const u: HelloHi = {
    hi() {},
    text: 't',
};
