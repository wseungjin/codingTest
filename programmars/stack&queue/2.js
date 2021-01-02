function solution(progresses, speeds) {
  const left = [];

  for (let i in progresses) {
    left.push(Math.ceil((100 - progresses[i]) / speeds[i]));
  }

  const stack = [];
  const answer = [];
  let currentIndex = 0;

  for (let value of left) {
    if (stack.length === 0) {
      stack.push(value);
      answer.push(1);
    } else if (stack[stack.length - 1] < value) {
      stack.push(value);
      answer.push(1);
      currentIndex += 1;
    } else if (stack[stack.length - 1] >= value) {
      answer[currentIndex] += 1;
    }
  }

  return answer;
}

function main() {
  console.log(solution([93, 30, 55], [1, 30, 5]));
  console.log(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]));
}

main();
