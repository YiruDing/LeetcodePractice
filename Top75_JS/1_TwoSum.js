// https://www.youtube.com/watch?v=pblq-fj137A&list=PLY5pAT_51eGw--pxzA_bd9ZHLuqfI_97E&index=1

function twoSum(nums, target) {
  let memory = {};

  for (let i = 0; i < nums.length; i++) {
    let currentValue = nums[i];
    if (memory[currentValue] === undefined) {
      memory[target - currentValue] = i;
    } else {
      return [memory[currentValue], i];
    }
  }
}
