class Solution:
    def confusingNumber(self, n: int) -> bool:
        res = []
        num = n
        if n == 0:
            return False
        invalids = ["2", "3", "4", "5", "7" ]
        while num > 0:
            pos = str(num % 10)
            if pos in invalids:
                return False
            if pos == "6":
                pos = "9"
            elif pos == "9":
                pos = "6"
            res.append(pos)
            num = num // 10
        res = int("".join(res))
        if res != n:
            return True
        return False