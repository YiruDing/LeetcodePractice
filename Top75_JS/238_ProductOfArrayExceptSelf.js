// https://www.youtube.com/watch?v=-3KG82kuD78&list=PLY5pAT_51eGw--pxzA_bd9ZHLuqfI_97E&index=5

function productExcaptSelf(nums) {
  let result = [];
  let rightProduct = [];
  let leftProduct = [];

  for (let i = 0; i < nums.length; i++) {
    if (leftProduct.length === 0) {
      leftProduct.push(1);
    } else {
      leftProduct.push(leftProduct[i - 1] * nums[i - 1]);
    }
  }
  for (let i = nums.length - 1; i > -1; i--) {
    if (rightProduct.length === 0) {
      rightProduct.push(1);
    } else {
      rightProduct.unshift(rightProduct[0] * nums[i + 1]);
      // rightProduct[0] a.k.a the latest product
    }
  }

  for (let i = 0; i < leftProduct.length; i++) {
    result.push(leftProduct[i] * rightProduct[i]);
  }
  return result;
}
