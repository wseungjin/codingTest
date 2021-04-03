function getRoute(train) {
  const newRoute = {};
  for (const route of train) {
    if (newRoute[route[0]] === undefined) {
      newRoute[route[0]] = [route[1]];
    } else {
      newRoute[route[0]].push(route[1]);
    }

    if (newRoute[route[1]] === undefined) {
      newRoute[route[1]] = [route[0]];
    } else {
      newRoute[route[1]].push(route[0]);
    }
  }
  return newRoute;
}
function dfs(current, before, visited, route, passenger, possibleAnswer) {
  let flag = false;
  for (const next of route[current]) {
    if (visited[next] === false) {
      flag = true;
      visited[next] = true;
      dfs(
        next,
        before + passenger[next - 1],
        visited,
        route,
        passenger,
        possibleAnswer
      );
      visited[next] = false;
    }
  }
  if (flag === false) possibleAnswer.push([current, before]);
}

function solution(n, passenger, train) {
  const route = getRoute(train);

  const visited = [];
  const possibleAnswer = [];

  for (let i = 0; i < n + 1; i++) {
    visited.push(false);
  }
  visited[1] = true;
  dfs(1, passenger[0], visited, route, passenger, possibleAnswer);

  possibleAnswer.sort();
  return possibleAnswer[possibleAnswer.length - 1];
}
console.log(
  solution(
    6,
    [1, 1, 1, 1, 1, 1],
    [
      [1, 2],
      [1, 3],
      [1, 4],
      [3, 5],
      [3, 6],
    ]
  )
);
console.log(
  solution(
    4,
    [2, 1, 2, 2],
    [
      [1, 2],
      [1, 3],
      [2, 4],
    ]
  )
);
console.log(
  solution(
    5,
    [1, 1, 2, 3, 4],
    [
      [1, 2],
      [1, 3],
      [1, 4],
      [1, 5],
    ]
  )
);
