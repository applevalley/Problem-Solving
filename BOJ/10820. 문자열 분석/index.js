const fs = require("fs");
const path = require("path");

const filePath = path.join(__dirname, "example.txt");

let input = fs
  .readFileSync(filePath)
  .toString()
  .split("\n")
  .map((line) => line.replace("\r", ""));

let answer = [];

for (let i in input) {
  //   if (input[i] === "") continue;
  const temp = [0, 0, 0, 0];

  for (let j in input[i]) {
    if (input[i][j].charCodeAt() >= 97 && input[i][j].charCodeAt() <= 122) {
      temp[0]++;
    }

    if (input[i][j].charCodeAt() >= 65 && input[i][j].charCodeAt() <= 90) {
      temp[1]++;
    }

    if (input[i][j].charCodeAt() >= 48 && input[i][j].charCodeAt() <= 57) {
      temp[2]++;
    }

    if (input[i][j].charCodeAt() === 32) {
      temp[3]++;
    }
  }

  answer.push(temp.join(" "));
}

console.log(answer.join("\n"));
