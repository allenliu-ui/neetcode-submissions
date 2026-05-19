class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        num0s = 0
        num1s = 0
        for pref in students:
            if (pref == 0):
                num0s += 1
            else:
                num1s += 1
        for pref in sandwiches:
            if (pref == 0 and num0s > 0):
                num0s -= 1
            elif (pref == 1 and num1s > 0):
                num1s -= 1
            else:
                break
        return num0s + num1s

        