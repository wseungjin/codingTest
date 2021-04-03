function combination(arr, m) {
  const combinations = [];
  const picked = [];
  const used = [];
  for (const item of arr) used.push(0);

  function find(picked) {
    if (picked.length === m) {
      const rst = [];
      for (let i of picked) {
        rst.push(arr[i]);
      }
      combinations.push(rst);
      return;
    } else {
      let start = picked.length ? picked[picked.length - 1] + 1 : 0;
      for (let i = start; i < arr.length; i++) {
        if (i === 0 || arr[i] !== arr[i - 1] || used[i - 1]) {
          picked.push(i);
          used[i] = 1;
          find(picked);
          picked.pop();
          used[i] = 0;
        }
      }
    }
  }
  find(picked);
  return combinations;
}

function isCorrect(need, candidate) {
  for (const needIndex of need) {
    if (candidate[needIndex] !== true) return false;
  }
  return true;
}

function transformNeeds(needs) {
  const newNeeds = [];

  for (const need of needs) {
    const newNeed = [];
    for (let i = 0; i < need.length; i++) {
      if (need[i] === 1) {
        newNeed.push(i);
      }
    }
    newNeeds.push(newNeed);
  }
  return newNeeds;
}

function transformCanditates(candidates) {
  const newCandidates = [];

  for (const candidate of candidates) {
    const newCandidate = {};
    for (const candidateIndex of candidate) {
      newCandidate[candidateIndex] = true;
    }
    newCandidates.push(newCandidate);
  }
  return newCandidates;
}

function solution(needs, r) {
  const [...keys] = Array(needs[0].length).keys();

  const candidates = combination(keys, r);
  const objectCandidates = transformCanditates(candidates);

  const transformedNeeds = transformNeeds(needs);

  let answer = 0;
  for (const candidate of objectCandidates) {
    let curValue = 0;
    for (const need of transformedNeeds) {
      if (isCorrect(need, candidate)) {
        curValue += 1;
      }
    }
    if (curValue > answer) {
      answer = curValue;
    }
  }
  return answer;
}

console.log(
  solution(
    [
      [1, 0, 0],
      [1, 1, 0],
      [1, 1, 0],
      [1, 0, 1],
      [1, 1, 0],
      [0, 1, 1],
    ],
    2
  )
);
