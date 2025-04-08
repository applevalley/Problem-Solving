const fs = require("fs");
const path = require("path");
const filePath = path.join(__dirname, "/dev/stdin");

let input = fs
  .readFileSync(filePath)
  .toString()
  .split("\n")
  .map((line) => line.replace("\r", ""));

let [n, ...words] = input;
let answer = 0;

for (let i = 0; i < n; i++) {
  if (words[i].length % 2) {
    continue;
  }

  const stack = [];
  const splittedWord = words[i].split("");
  for (let j = 0; j < splittedWord.length; j++) {
    if (stack[stack.length - 1] === splittedWord[j]) {
      stack.pop();
      continue;
    }

    if (stack[stack.length - 1] !== splittedWord[j]) {
      stack.push(splittedWord[j]);
      continue;
    }
  }

  if (!stack.length) {
    answer++;
  }
}

console.log(answer);
