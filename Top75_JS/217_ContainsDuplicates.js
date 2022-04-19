// https://www.youtube.com/watch?v=tVr0xWxnX14&list=PLY5pAT_51eGw--pxzA_bd9ZHLuqfI_97E&index=2

// solution#1
function containsDuplicate(nums) {
  let memory = {};
  for (let i = 0; i < nums.length; i++) {
    let currentValue = nums[i];
    if (!memory[currentValue]) {
      memory[currentValue] = 1;
    } else {
      return true;
    }
  }
  return false;
}

// solution#1
function containsDuplicate(nums) {
  nums.sort((a, b) => a - b);
  for (let i = 0; i < nums.length; i++) {
    if (i > 0 && nums[i - 1] === nums[i]) {
      return true;
    }
  }
  return false;
}
