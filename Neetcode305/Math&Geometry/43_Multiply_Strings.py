class Solution:

    def multiply(self, num1: str, num2: str) -> str:
        if "0" in [num1, num2]:
            return "0"

        res = [0] * (len(num1) + len(num2))
        num1, num2 = num1[::-1], num2[::-1]
        # 4/12 勿忘上面這一行！

        for i1 in range(len(num1)):
            for i2 in range(len(num2)):
                digit = int(num1[i1]) * int(num2[i2])
                res[i1 + i2] += digit
                # 16:54 res[i1 + i2] may be two digit
                # 10/7儲存在這裡是為了之後可以用到
                res[i1 + i2 + 1] += res[i1 + i2] // 10
                res[i1 + i2] = res[i1 + i2] % 10
                # 上一行亦可作 res[i1 + i2] %= 10
                # e.g. 8 * 12

        res, begin = res[::-1], 0
        while begin < len(res) and res[begin] == 0:
            begin += 1
        res = map(str, res[begin:])
        # map(fun, iter)
        # input"2" "3"
        # res before being joined:  <map object at 0x7f220442b2e0>
        # 十六進位(Hex)

        return "".join(res)