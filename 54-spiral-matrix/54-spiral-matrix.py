class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        def check4(numbers,matrix):
            if not len(matrix):
                return numbers
            l = len(matrix)
            i = l -1
            while i >-1:
                numbers.append(matrix[i].pop(0))
                if not len(matrix[i]):
                    matrix.pop(i)
                i -= 1
            return check1(numbers, matrix)

        def check3(numbers, matrix):
            if not len(matrix):
                return numbers
            l = len(matrix) - 1
            matrix[l].reverse()
            numbers += matrix.pop()
            return check4(numbers,matrix)

        def check2(numbers, matrix):
            if not len(matrix):
                return numbers
            l = len(matrix)
            i = 0
            while i < l:
                numbers.append(matrix[i].pop())
                if not len(matrix[i]):
                    matrix.pop(i)
                    i -= 1
                    l -= 1
                i += 1
            return check3(numbers, matrix)


        def check1(numbers, matrix):
            if not len(matrix):
                return numbers
            numbers += matrix[0]
            matrix.pop(0)
            return check2(numbers, matrix)
        
        numbers = list()
        return check1(numbers, matrix)