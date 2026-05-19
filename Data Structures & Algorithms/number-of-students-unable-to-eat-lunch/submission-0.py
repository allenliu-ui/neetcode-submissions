class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        while (len(students) > 0):
            if ((0 not in students and sandwiches[0] == 0) or (1 not in students and sandwiches[0] == 1)):
                return len(students)
            if (students[0] == sandwiches[0]):
                students.pop(0)
                sandwiches.pop(0)
            else:
                unhappyStudent = students.pop(0)
                students.append(unhappyStudent)
        return 0
        