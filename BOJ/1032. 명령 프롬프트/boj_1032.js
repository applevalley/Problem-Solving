const fs = require("fs");
const path = require("path");
const filePath = path.join(__dirname, "/dev/stdin");

let input = fs
  .readFileSync(filePath)
  .toString()
  .split("\n")
  .map((line) => line.replace("\r", ""));

let answer = "";

const stringOnlyArray = input.filter((item) => isNaN(Number(item)));
const maxLength = stringOnlyArray[0].length;

// 각 위치별로 문자 묶기
const regroupedArray = [];
for (let i = 0; i < maxLength; i++) {
  const charGroup = stringOnlyArray.map((str) =>
    i < str.length ? str[i] : ""
  );
  regroupedArray.push(charGroup);
}

regroupedArray.forEach((charGroup) => {
  // 첫 번째 문자를 기준으로 모든 문자가 동일한지 확인
  const firstChar = charGroup[0];
  const allSame = charGroup.every((char) => char === firstChar);

  // 모든 문자가 동일하면 해당 문자를, 아니면 '?'를 answer에 추가
  if (allSame) {
    answer += firstChar;
  } else {
    answer += "?";
  }
});

console.log(answer);
