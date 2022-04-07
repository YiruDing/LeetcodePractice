function search(nums, target) {
  while (target) {
    nums.pop().shift();
    target--;
  }

  for (let i = 0; i < nums.length; i++) {
    if (nums[i] === target) {
      return i;
    }
  }
  return -1;
}
