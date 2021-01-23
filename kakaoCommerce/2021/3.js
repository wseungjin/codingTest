function solution(next_student) {
  const value = Array(next_student.length).fill(1);

  let maxValue = 0;
  let answer = 0;

  for (let i = 0; i < next_student.length; i++) {
    const visited = Array(next_student.length).fill(false);
    let start = i;
    let next = next_student[i] - 1;

    visited[start] = true;
    while (next !== -1 && visited[next] === false) {
      start = next;
      visited[start] = true;
      next = next_student[start] - 1;
      value[i] += 1;
    }

    if (maxValue <= value[i]) {
      maxValue = value[i];
      answer = i;
    }
  }
  return answer + 1;
}

console.log(solution([5, 9, 13, 1, 0, 0, 11, 1, 7, 12, 9, 9, 2]));
console.log(solution([6, 10, 8, 5, 8, 10, 5, 1, 6, 7]));
