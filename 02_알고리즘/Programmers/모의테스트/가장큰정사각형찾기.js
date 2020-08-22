function solution(board)
{
    let ans = 0
    
    // 한변의 길이가 1이고, 해당 직사각형안에 1이 있는경우에는 1을 반환한다.
    // 만약 0만 있을 경우 아래 반복문이 진행되지 않기 때문에 0을 반환
    if (board.length<2 &&board.includes(1)){
        return 1
    }
    if (board[0].length<2 && board[0].filter(x=> x===1).length){
        return 1
    }
    
    //아닐경우 DP진행 
    for(let i = 1; i<board.length; i++){
        for (let j = 1 ; j< board[i].length; j++){
            if (board[i][j]){
                board[i][j] = Math.min(board[i-1][j], board[i][j-1], board[i-1][j-1])+1
            }
            if (ans <board[i][j]) ans = board[i][j]
        }
    }
    
    return ans*ans
}
console.log(solution([[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]))
