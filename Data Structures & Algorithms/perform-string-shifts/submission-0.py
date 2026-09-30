class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        for shift_direction, shift_amount in shift:
            if shift_direction == 0:
                while shift_amount > 0:
                    temp = s[0]
                    s = s[1:]
                    s = s + temp
                    shift_amount -= 1
            else:
                while shift_amount > 0:
                    temp = s[-1]
                    s = s[:len(s) - 1]
                    s = temp + s
                    shift_amount -= 1
        return s