const object = { a: 1, b: 2 };

const { a, b } = object;

console.log(a); //1
console.log(b); //2

function print({ a, b }) {
    console.log(a);
    console.log(b);
}
print(object)


console.log('======================')


const object2 = { c: 3 };
const { c } = object2;
const { d = 4 } = object2;
console.log(c)
console.log(d)


console.log('======================')
const animal = { name: '멍멍이', type: '개' };

const { name: nickname } = animal;

console.log(nickname)
// console.log(name) name is not defined, animal 객체 내부의 name을 nickname이라고 선언.

console.log('======================')
//비구조화 할당은 배열에서도 가능함
const arr = [1, 2];
const [one, two] = arr;

console.log(one);
console.log(two)


console.log('========== ES6: object-shorhand ============');
//깊은 값 비구조화 할당
const deepObject = {
    state: {
        info: {
            name: 'mini',
            lang: ['python', 'javaScript', 'C', 'C++']
        }
    },
    value: 3
}

const { name, lang } = deepObject.state.info;
const { value } = deepObject

console.log(name);
console.log(lang);

const extract = {
    name,
    lang,
    value
}

console.log(extract)
