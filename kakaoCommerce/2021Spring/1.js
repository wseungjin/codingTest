function solution(gift_cards, wants) {
  const gift_dict = {};
  const wants_dict = {};

  gift_cards.forEach((element) => {
    if (element in gift_dict) {
      gift_dict[element] += 1;
    } else {
      gift_dict[element] = 1;
    }
  });

  wants.forEach((element) => {
    if (element in wants_dict) {
      wants_dict[element] += 1;
    } else {
      wants_dict[element] = 1;
    }
  });

  let solved = 0;

  for (const key in wants_dict) {
    const curWantValue = wants_dict[key];
    const curGiftValue = gift_dict[key] ? gift_dict[key] : 0;

    if (curGiftValue >= curWantValue) {
      solved += curWantValue;
    } else {
      solved += curGiftValue;
    }
  }
  return gift_cards.length - solved;
}
console.log(solution([4, 5, 3, 2, 1], [2, 4, 4, 5, 1]));

console.log(solution([5, 4, 5, 4, 5], [1, 2, 3, 5, 4]));
