function solution(bridge_length, weight, truck_weights) {
  //현재 다리 상태 (대기상태 queue)
  let doing = new Array(bridge_length).fill(0);
  //경과시간
  let cnt = 0;
  // 현재 지나는 다리
  let current_truck = truck_weights.shift();
  //현재 다리 무게
  let total_weight = 0;

  doing.unshift(current_truck);
  doing.pop();

  total_weight += current_truck;
  cnt++;

  while (total_weight) {
    total_weight -= doing.pop();
    current_truck = truck_weights.shift();
    if (current_truck + total_weight <= weight) {
      doing.unshift(current_truck);
      total_weight += current_truck;
    } else {
      doing.unshift(0);
      truck_weights.unshift(current_truck);
    }
    cnt++;
  }
  return cnt;
}
