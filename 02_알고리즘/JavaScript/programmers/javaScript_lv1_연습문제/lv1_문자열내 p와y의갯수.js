function solution(s) {
  var p_cnt = 0,
    y_cnt = 0;
  p_cnt = s.toLowerCase().split("p");
  y_cnt = s.toLowerCase().split("y");

  if (p_cnt.length === y_cnt.length) {
    return true;
  } else {
    return false;
  }
}

function solution(s){
  let p_cnt = s.toLowerCase().split('').filter(x=>x==='p').length
  let y_cnt = s.toLowerCase().split('').filter(x=>x==='y').length

  return (p_cnt === y_cnt)? true: false
}