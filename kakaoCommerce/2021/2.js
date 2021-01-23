function solution(m, v) {
  const layer = new Array(100000);
  let top = 0;
  let bottom = 0;

  for (let i = 0; i < v.length; i++) {
    let possibleBottom = top;
    for (let j = top - 1; j >= bottom; j--) {
      if (layer[j] + v[i] <= m) {
        possibleBottom = j;
      } else break;
    }

    let flag = true;
    for (let j = possibleBottom; j < top; j++) {
      if (layer[j] + v[i] <= m) {
        layer[j] = layer[j] + v[i];
        if (layer[j] === m) {
          bottom = j + 1;
        }
        flag = false;
        break;
      }
    }

    if (flag) {
      layer[top] = v[i];
      top += 1;
      if (v[i] === m) {
        bottom = top;
      }
    }
  }
  return top;
}

console.log(solution(4, [2, 3, 1]));
console.log(solution(4, [3, 2, 3, 1]));
console.log(solution(4, [1, 1, 1, 1, 1]));
console.log(solution(4, [1, 1, 1, 4, 1, 3, 4]));
