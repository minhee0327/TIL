const debug1 = require('./debug')('one')
const debug2 = require('./debug')('two')
//debug1, debug2 로 두번 import 했지만, 노드앱을 실행할때 같은 모듈은 단 한번 import 된다.
//두번 import 해오더라도, 이미 해당 모듈을 import 했을을 인식하고 더이상 임포트하지 않는다.
//성능, 메모리 사용량, 관리 편리성을 위해 모듈은 단 한번만 임포트하는 것이 낫다.

//결과를 예측해보기!
debug1(`started firts debugger!`)
debug2(`started second debugger!`)

setTimeout(function () {
    debug1(`after some time...`);
    debug2(`what happen?!`);
}, 200)


/*
//약간의 오차 있을 수 있음.
one started firts debugger! +0ms
two started second debugger! +6ms
one after some time... +203ms
two what happen?! +1ms
*/