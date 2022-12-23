class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        result = 0
        for op_item in operations:
            if op_item[1] == '+':
                result += 1
            else:
                result -= 1
        return result
