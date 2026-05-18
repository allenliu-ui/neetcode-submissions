class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        sum = 0
        for operation in operations:
            if (operation == "D"):
                record.append(record[len(record) - 1] * 2)
            elif (operation == "C"):
                record.pop(len(record) - 1)
            elif (operation == "+"):
                record.append(record[len(record) - 1] + record[len(record) - 2])
            else:
                record.append(int(operation))
        for num in record:
            sum += num
        return sum
