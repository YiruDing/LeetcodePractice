// https://www.youtube.com/watch?v=FMa1t8NYDbQ&list=PLY5pAT_51eGw--pxzA_bd9ZHLuqfI_97E&index=3
function maxProfit(prices) {
  let buyPrice = prices[0];
  let profit = 0;

  for (let i = 0; i < prices.length - 1; i++) {
    let tempProfit = prices[i + 1] - prices[i];
    if (tempProfit > 0) {
      if (prices[i] < buyPrice) {
        buyPrice = prices[i];
      }
      if (prices[i + 1] - buyPrice > profit) {
        profit = prices[i + 1] - buyPrice;
      }
    }
  }
  return profit;
}
