# prefix tree == trie
class Solution:

    def suggestedProducts(self, products: List[str],
                          searchWord: str) -> List[List[str]]:
        res = []
        products.sort()

        l, r = 0, len(products) - 1
        for i in range(len(searchWord)):
            c = searchWord[i]

            while l <= r and (len(products[l]) <= i or products[l][i] != c):
                # len(products[l]) 是個字，我們要確認他有沒有ith character
                l += 1
            while l <= r and (len(products[r]) <= i or products[r][i] != c):
                r -= 1
            # then we'll get a matching prefix

            res.append([])
            remain = r - l + 1
            # 這是剩下的字數，不是單個字母的數目
            for j in range(min(3, remain)):
                res[-1].append(products[l + j])
        return res
