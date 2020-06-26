// spread
const slime = {
    name: 'slime'
}
const cuteslime = {
    ...slime,
    attribute: 'cute'
}
const purpleCuteSlime = {
    ...cuteslime,
    color: 'purple'
}

console.log(slime);
console.log(cuteslime);
console.log(purpleCuteSlime);

const animals = ['개', '고양이', '참새'];
//spread 여러번 사용가능
const anotherAnimals = [...animals, '비둘기', ...animals];
console.log(animals);
console.log(anotherAnimals);


console.log('-----------------rest-------------------')
//rest
const cutePuppy = {
    name: '멍뭉이',
    attribute: 'cute',
    color: 'white'
}
const { color, ...rest } = cutePuppy;

console.log(color);
console.log(rest); //color를 제외한 나머지

const { attribute, ...name } = rest;
console.log(attribute);
console.log(name);



console.log('----------------- 배열 rest-------------------');
const numbers = [0, 1, 2, 3, 4, 5, 6]
const [one, ...rest_num] = numbers // 이거 사용할때, rest가 앞에 오면 syntaxError발생함

console.log(one);
console.log(rest_num);

const numnum = [...rest_num, ...rest_num]
console.log(numnum)

// console.log(Math.max(...numbers))