strs = ["eat", "tea", "tan", "ate", "nat", "bat"];
// Output: [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]];

function solution(arr) {
  let obj = {};

  for (let word of arr) {
    let s_sort = word.toLowerCase().split("").sort().join("");

    if (obj.hasOwnProperty(s_sort)) {
      obj[s_sort].push(word);
    } else {
      obj[s_sort] = [word];
    }
  }
  return Object.values(obj);
}

let answer = solution(strs);
console.log(answer);
