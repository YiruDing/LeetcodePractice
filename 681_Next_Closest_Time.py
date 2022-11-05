class Solution:

    def nextClosestTime(self, time: str) -> str:
        hh = int(time[0:2])
        mm = int(time[3:5])
        # get current digits
        digits = set()
        for d in time:
            if d != ':':
                digits.add(ord(d) - ord('0'))
        # try possible closest time one by one
        for _ in range(1440):
            # 一次加一，如果四位數都在digits內，即可return
            hh, mm = self.addOne(hh, mm)
            # whether all the digits are reused
            if self.areDigitsIn(digits, hh, mm):
                return '{0:0>2}:{1:0>2}'.format(hh, mm)
                # >右對齊，補在右邊 寬度二
                # >左對齊，補在左邊 寬度二
                


# e.g.:
# print "{0:=>+011.3f};".format(12.12345)
# #====+12.123;用=来填充,右对齐,因为已经用=来填充了,0无效,宽度11,小数点精度后精度为3,类型为浮点数
        return time

    def addOne(self, hh, mm):
        # add one minite to current time
        mm += 1
        # hh不要加！
        if mm == 60:
            hh += 1
            mm = 0
            # mm = 0
        if hh == 24:
            hh = 0
        return hh, mm

    def areDigitsIn(self, digits, hh, mm):
        # whether the digits in time hh:mm are all in given digits
        h1, h2 = hh // 10, hh % 10
        m1, m2 = mm // 10, mm % 10
        return h1 in digits and h2 in digits and m1 in digits and m2 in digits