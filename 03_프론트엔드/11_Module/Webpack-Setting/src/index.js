import 'normalize.css';
import styles from './index.module.scss'
import $ from 'jquery';
// import cuteImg from './images/cute.png'
// import chickenImg from './images/chicken.svg';
import webpackImg from './images/webpack.svg'
import '@babel/polyfill';

function component() {
    const element = document.createElement('div'); //div tag를 생성
    element.innerText = "Hello Webpack"; //div 태그 내부 글자

    // const imgElement = document.createElement('img');
    // imgElement.src = cuteImg;
    // imgElement.classList = styles.cuteImg

    // const imgElement2 = document.createElement('img');
    // imgElement2.src = chickenImg;
    // imgElement2.classList = styles.chickenImg

    const imgElement3 = document.createElement('img');
    imgElement3.src = webpackImg;
    imgElement3.classList = styles.webpackImg

    // console.log(cuteImg);
    // console.log(chickenImg);
    console.log(styles);

    // element.appendChild(imgElement);
    // element.appendChild(imgElement2);
    element.appendChild(imgElement3);

    element.classList = styles.helloWebpack //div 태그 내부에 클래스로 helloWebpack의 해시값

    return element;
}

document.body.appendChild(component()) //body태그 자식요소로 component함수로 만든 div태그를 붙임

//따라서 결과: class에 있는 css우선순위가 일반 태그에 적용한 것보다 높기 때문에 파랑색 출력
//console.log(styles); => {helloWebpack: 해시값} 

//벤더 chunk hash test 용도(사용 vendor: jQuery)
console.log($(`.${styles.helloWebpack}`).length);

//production mode 인지 확인(npm run build 할 경우, true가 나옴)
console.log(`IS_PRODUCTION MODE: ${IS_PRODUCTION}`)