function solution(next_student) {
  const value = Array(next_student.length).fill(1);

  let maxValue = 0;
  let answer = 0;

  for (let i = 0; i < next_student.length; i++) {
    if (value[i] === 1) {
      const visited = Array(next_student.length).fill(false);
      let start = i;
      let next = next_student[i] - 1;
      const path = [start];
      let current = 1;

      visited[start] = true;
      while (next !== -1 && visited[next] === false) {
        if (value[next] !== 1) {
          current += value[next];
          break;
        }

        start = next;
        visited[start] = true;
        path.push(start);
        next = next_student[start] - 1;
        current += 1;
      }

      if (maxValue <= current) {
        maxValue = current;
        answer = i;
      }

      let flag = false;
      for (let j = 0; j < path.length; j++) {
        if (path[j] === next) {
          flag = true;
        }
        if (flag === false) {
          value[path[j]] = current;
          current -= 1;
        } else {
          value[path[j]] = current;
        }
      }
    }
  }
  return answer + 1;
}

console.log(solution([2, 3, 1, 1]));
console.log(solution([2, 3, 4, 0]));
console.log(solution([5, 9, 13, 1, 0, 0, 11, 1, 7, 12, 9, 9, 2]));
console.log(solution([6, 10, 8, 5, 8, 10, 5, 1, 6, 7]));
