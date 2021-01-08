//m 이상, n이하 무작위 정수 반환
function rand(m, n) {
  return m + Math.floor((n - m + 1) * Math.random());
}

function randFace() {
  return ["crown", "anchor", "heart", "spade", "club", "diamond"][rand(0, 5)];
}

let funds = 50; // 판돈 (50 으로 시작)
let round = 0; // 게임을 몇판 진행중인지

while (funds > 1 && funds < 100) {
  round++;
  console.log(`round: ${round}`);
  console.log(`\tStarting funds: ${funds}`);

  //돈을 건다. (6모양의 카드 중 건 금액 체크)
  let bets = { crown: 0, anchor: 0, heart: 0, spade: 0, club: 0, diamond: 0 };
  let totalBet = rand(1, funds);

  if (totalBet === 7) {
    //7은 행운의 숫자라고 생각해서 판돈을 모두 하트에 걸것.
    totalBet = funds;
    bets.heart = totalBet;
  } else {
    //판돈 나누기
    let remaining = totalBet;
    do {
      let bet = rand(1, remaining);
      let face = randFace();
      bets[face] += bet;
      remaining -= bet;
    } while (remaining > 0);
  }

  funds = funds - totalBet;
  console.log(
    "\tbets: " +
      Object.keys(bets)
        .map((face) => `${face}: ${bets[face]} pence`)
        .join(", ") +
      ` (total: ${totalBet}pence)`
  );

  //주사위를 굴린다.
  const hand = [];
  for (let i = 0; i < 3; i++) {
    hand.push(randFace());
  }
  console.log(`\thand: ${hand.join(", ")}`);

  let winnings = 0;

  for (let i = 0; i < hand.length; i++) {
    let face = hand[i];
    if (bets[face] > 0) winnings += bets[face];
  }
  funds = funds + winnings;
  console.log(`\twinnings funds: ${funds}`);
}

console.log(`ending funds: ${funds}`);
