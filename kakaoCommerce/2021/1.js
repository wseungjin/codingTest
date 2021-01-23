function solution(n, record) {
  const answer = [];

  const object = {};

  for (let i = 0; i < n; i++) {
    object[i] = [];
  }

  for (let i = 0; i < record.length; i++) {
    let [sNum, name] = record[i].split(" ");
    sNum -= 1;
    let flag = true;
    for (let j = 0; j < object[sNum].length; j++) {
      if (object[sNum][j] === name) {
        flag = false;
      }
    }

    if (flag) {
      if (object[sNum].length == 5) {
        object[sNum].shift();
      }
      object[sNum].push(name);
    }
  }

  for (let i = 0; i < n; i++) {
    for (const name of object[i]) {
      answer.push(name);
    }
  }

  return answer;
}

console.log(
  solution(1, [
    "1 fracta",
    "1 sina",
    "1 hana",
    "1 robel",
    "1 abc",
    "1 sina",
    "1 lynn",
  ])
);

console.log(
  solution(4, [
    "1 a",
    "1 b",
    "1 abc",
    "3 b",
    "3 a",
    "1 abcd",
    "1 abc",
    "1 aaa",
    "1 a",
    "1 z",
    "1 q",
    "3 k",
    "3 q",
    "3 z",
    "3 m",
    "3 b",
  ])
);
