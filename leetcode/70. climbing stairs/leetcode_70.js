/**
 * @param {number} n
 * @return {number}
 */

var climbStairs = function (n) {
  const memo = {};

  function climb(i) {
    if (i > n) return 0;
    if (i === n) return 1;
    if (i in memo) return memo[i];

    memo[i] = climb(i + 1) + climb(i + 2);
    return memo[i];
  }

  return climb(0);
};
