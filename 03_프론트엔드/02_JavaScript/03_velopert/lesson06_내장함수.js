//forEach
console.log('----------for each----------')
const superhero = ['ironman', 'spiderman', 'captainAmerica'];
superhero.forEach(hero => console.log(hero));

//map
//파라미터로 변화를 주는 함수 전달.
console.log('---------- map ----------');
const array = [1, 2, 3, 5, 6];
console.log(array.map(n => n * n));

//index of
//원하는 항목이 몇번째 원소인지 찾아주는 함수
console.log('------- index of --------');
const animal = ['dog', 'cat', 'lion', 'mouse']
console.log(animal.indexOf('cat'));

//findIndex
//배열 내부에 객체가 있을 때, 
//검사하고자 하는 조건을 반환하는 함수를 넣어 찾기
console.log('------- findIndex --------');
const todos = [
    {
        id: 1,
        text: '자바스크립트 입문',
        done: true
    },
    {
        id: 2,
        text: '함수 배우기',
        done: true
    },
    {
        id: 3,
        text: '객체와 배열 배우기',
        done: true
    },
    {
        id: 4,
        text: '배열 내장함수 배우기',
        done: false
    }
];

const index = todos.findIndex(todo => todo.id === 3);
console.log(index)

//find
// 찾아낸 값이 몇번째인지 알아내는 것이 아니고, 찾아낸 값 자체 반환
console.log('------- find --------');
const todo = todos.find(todo => todo.id === 3);
console.log(todo);


//filter
// 배열에서 특정 조건을 만족하는 값들만 따로 추출하여 새로운 배열을 만듬
console.log('------- filter --------');
const taskNotDone = todos.filter(todo => todo.done === false);
const taskNotDone2 = todos.filter(todo => !todo.done);
const taksDone = todos.filter(todo => todo.done === true);
console.log('todo.done값이 false 일때만 해당 객체를 배열에 담아 반환')
console.log(taskNotDone);
console.log(taskNotDone2);
console.log('todo.done값이 true일때만 해당 객체를 배열에 담아 반환')
console.log(taksDone);


//splice
//배열에서 특정 항목을 제거할 때 사용
//splice(start_index, 몇개지을지)
console.log('------- splice --------');
const numbers = [10, 20, 30, 40]
const idx = numbers.indexOf(30)
console.log(numbers.splice(idx, 1));
console.log(numbers)

//slice
//기존 배열을 건드리지 않음
// 첫번째 파라미터: 어디서부터 자를지
// 두번째 파라미터: 어디까지 자를지
console.log('------------ slice ----------');
const numbers1 = [10, 20, 30, 40]
const sliced = numbers1.slice(0, 2);
console.log(sliced);
console.log(numbers1);

// reduce
// 첫번째 파라미터로 누적된값, 현재 값을 전달하는 콜백함수, 
// 2번째 파라미터로 reduce함수에서 사용할 초기값
console.log('------------ reduce ----------');
const numbers2 = [1, 2, 3, 4, 5];
// let sum = numbers2.reduce((accumulator, current)=> accumulator+ current, 0)
let sum = numbers2.reduce((accumulator, current) => {
    console.log({ accumulator, current })
    return accumulator + current
}, 0)
console.log('합계: ', sum);


//reduce함수로 평균값 구하기
let avg = numbers2.reduce((accumulator, current, index, array) => {
    if (index == array.length - 1) {
        return (accumulator + current) / array.length
    }
    return accumulator + current;
}, 0)
console.log('평균값: ', avg)


console.log('------------ includes ----------');
const animals = ['냐옹이', '멍뭉이', '거북이', '너구리'];
console.log(animals.includes('거북이'));
console.log(animals.includes('노트북'));


// 자주 사용되는 내장함수 키워드 정리
// shift, pop 
// unshift, push
// concat: 배열 이어줄때
// join : 배열 => 문자열 [사용시 예제: array.join('')]
