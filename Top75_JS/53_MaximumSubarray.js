function maxSubArray(nums) {
  let maxValue = nums[0];
  let accNum = nums[0];
  for (let i = 1; i < nums.length; i++) {
    let calc = Math.max(nums[i], accNum + nums[i]);
    if (calc > maxValue) maxValue = calc;
    accNum = calc;
  }
  return maxValue;
}
