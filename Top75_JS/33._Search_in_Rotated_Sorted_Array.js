// https://www.youtube.com/watch?v=A7dT6UtWEhA

function search(nums, target) {
  let left = 0;
  let right = nums.length - 1;

  while (left <= right) {
    let mid = Math.floor(left + (right - left) / 2);

    if (nums[mid] === target) {
      return mid;
    }
    if (nums[left] <= nums[mid]) {
      // Which means the left part is sorted
      if (nums[mid] > target && nums[left] <= target) right = mid - 1;
      else left = mid + 1;
    } else {
      if (nums[mid] < target && nums[right] >= target) left = mid + 1;
      else right = mid - 1;
    }
  }

  return -1;
}
