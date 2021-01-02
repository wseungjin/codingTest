function isInclude(totalTokens, targetTokens) {
  const totalSize = totalTokens.length;
  const targetSize = targetTokens.length;

  for (let i = 0; i < totalSize; i++) {
    if (i + targetSize > totalSize) {
      break;
    }
    let flag = true;
    for (let j = 0; j < targetSize; j++) {
      if (totalTokens[i + j] !== targetTokens[j]) {
        flag = false;
      }
    }
    if (flag) return true;
  }
  return false;
}

function solution(m, musicinfos) {
  const regPattern = /C#|C|D#|D|E#|E|F#|F|G#|G|A#|A|B/;

  const targetTokens = [];
  let targetString = m;

  while (targetString !== "") {
    const result = regPattern.exec(targetString);

    if (result[0] != null) {
      targetTokens.push(result[0]);
    }
    // move to next string
    const newIndex = result[0].length;
    targetString = targetString.slice(newIndex).replace(" ", "");
  }

  const splitedMusicData = [];

  for (const musicinfo of musicinfos) {
    const splitedMusicInfo = musicinfo.split(",");

    const beforeTime = splitedMusicInfo[0].split(":");
    const afterTime = splitedMusicInfo[1].split(":");
    const musicName = splitedMusicInfo[2];
    const musicString = splitedMusicInfo[3];

    const hours = parseInt(afterTime[0]) - parseInt(beforeTime[0]);
    const minutes = parseInt(afterTime[1]) - parseInt(beforeTime[1]);

    const totalTime = hours * 60 + minutes;

    splitedMusicData.push([totalTime, musicName, musicString]);
  }

  splitedMusicData.sort(function (a, b) {
    if (a[0] > b[0]) {
      return -1;
    }
    if (a[0] < b[0]) {
      return 1;
    }
    // a must be equal to b
    return 0;
  });

  for (const musicinfo of splitedMusicData) {
    const totalTime = musicinfo[0];
    const musicName = musicinfo[1];
    let musicString = musicinfo[2];

    const musicTokens = [];
    while (musicString !== "") {
      const result = regPattern.exec(musicString);

      if (result[0] != null) {
        musicTokens.push(result[0]);
      }
      // move to next string
      const newIndex = result[0].length;
      musicString = musicString.slice(newIndex).replace(" ", "");
    }

    const musicLength = musicTokens.length;
    let totalTokens = [];

    const repeat = parseInt(totalTime / musicLength);
    const left = totalTime % musicLength;

    for (let i = 0; i < repeat; i++) {
      totalTokens = totalTokens.concat(musicTokens);
    }
    if (left > 0) {
      totalTokens = totalTokens.concat(musicTokens.slice(0, left));
    }

    if (isInclude(totalTokens, targetTokens)) {
      return musicName;
    }
  }
  return "(None)";
}
function main() {
  console.log(
    solution("ABCDEFG", [
      "13:50,14:00,WORLD,ABCDEF",
      "12:00,12:14,HELLO,CDEFGAB",
    ])
  );
  console.log(
    solution("CC#BCC#BCC#BCC#B", [
      "03:00,03:30,FOO,CC#B",
      "04:00,04:08,BAR,CC#BCC#BCC#B",
    ])
  );
  console.log(
    solution("ABC", ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"])
  );
  console.log(solution("ABC", ["0:00,00:05,HI,ABC#ABC"]));
  console.log(solution("ABC", ["0:00,00:06,HI,ABC#ABC"]));
}

main();
