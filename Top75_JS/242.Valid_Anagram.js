var isAnagram = function (s, t) {
  if (s.length !== t.length) return false;
  let count = {};
  for (let i = 0; i < s.length; i++) {
    let currentCha = s[i];
    if (!count[currentCha]) {
      count[currentCha] = 1;
    } else {
      count[currentCha]++;
    }
  }
  for (let i = 0; i < t.length; i++) {
    let currentCha = t[i];
    if (!count[currentCha]) {
      return false;
    } else {
      count[currentCha]--;
    }
  }

  return (count = {} ? true : false);
};
