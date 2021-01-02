let answer = 0;

function dfs(count, currentValue, numbers, target) {
  if (count === numbers.length) {
    if (target === currentValue) {
      answer += 1;
    }
    return;
  }

  dfs(count + 1, currentValue + numbers[count], numbers, target);
  dfs(count + 1, currentValue - numbers[count], numbers, target);
}

function solution(numbers, target) {
  dfs(0, 0, numbers, target);
  return answer;
}

function main() {
  console.log(solution([1, 1, 1, 1, 1], 3));
}

main();
