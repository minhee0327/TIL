function solution(v) {
    let ans = []
    let row = v.map((x)=> x[0]).sort()
    let col = v.map((x)=> x[1]).sort()
    row[0] === row[1] ? ans.push(row[2]) : ans.push(row[0])
    col[0] === col[1] ? ans.push(col[2]) : ans.push(col[0])
    
    return ans   
}

/*
- 직사각형 꼭지점 3개를 배열(v)로 주어졌을때, 나머지 한 점 찾기 문제
*/