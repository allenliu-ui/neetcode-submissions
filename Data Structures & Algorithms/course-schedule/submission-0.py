class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses = [0] * numCourses
        coursesTaken = 0
        requisites = [[] for i in range(numCourses)]
        for course, prereq in prerequisites:
            courses[course] += 1
            requisites[prereq].append(course)
        queue = [i for i in range(numCourses) if courses[i] == 0]
        while queue:
            course = queue.pop(0)
            coursesTaken += 1
            for prereq in requisites[course]:
                courses[prereq] -= 1
                if courses[prereq] == 0:
                    queue.append(prereq)
        return coursesTaken == numCourses
                