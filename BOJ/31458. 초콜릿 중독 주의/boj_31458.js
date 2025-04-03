const fs = require("fs");
const path = require("path");
const filePath = path.join(__dirname, "/dev/stdin");

let input = fs
  .readFileSync(filePath)
  .toString()
  .split("\n")
  .map((line) => line.replace("\r", ""));

input.shift();

function facto(word) {
  if (word === "!0") return "1";
  if (word === "!1") return "0";
  if (word === "0!") return "1";
  if (word === "1!") return "1";
  // 오른쪽에서 왼쪽으로 순서대로 패턴을 찾아 처리

  // 1. 먼저 x! 패턴 찾기 (오른쪽 ! 연산자가 우선)
  for (let i = word.length - 2; i >= 0; i--) {
    if ((word[i] === "0" || word[i] === "1") && word[i + 1] === "!") {
      const leftPart = word.substring(0, i);
      const pattern = word.substring(i, i + 2);
      const rightPart = word.substring(i + 2);

      const result = pattern === "0!" ? "1" : "1"; // 0! -> 1, 1! -> 1
      const newStr = leftPart + result + rightPart;

      return facto(newStr);
    }
  }

  // 2. 다음으로 !x 패턴 찾기
  for (let i = word.length - 2; i >= 0; i--) {
    if (word[i] === "!" && (word[i + 1] === "0" || word[i + 1] === "1")) {
      const leftPart = word.substring(0, i);
      const pattern = word.substring(i, i + 2);
      const rightPart = word.substring(i + 2);

      const result = pattern === "!0" ? "1" : "0"; // !0 -> 1, !1 -> 0
      const newStr = leftPart + result + rightPart;

      return facto(newStr);
    }
  }

  return word; // 패턴을 찾지 못한 경우
}

function transformToPattern(word) {
  // 이미 최종 패턴 중 하나인 경우
  if (["!0", "!1", "0!", "1!"].includes(word)) {
    return word;
  }

  return facto(word);
}

input.forEach((example) => {
  const result = transformToPattern(example);
  console.log(facto(result));
});
