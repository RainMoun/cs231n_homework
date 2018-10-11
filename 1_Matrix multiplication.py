# author: RainMoun
# content: 矩阵乘法


class Matrix:
    def __init__(self, lst):
        self.matrix = lst
        self.row = len(lst)  # 矩阵长
        if lst[0]:
            self.column = len(lst[0])  # 矩阵宽
        else:
            self.column = 0

    def matrix_multiplication(self, others):
        result_value = [[0] * self.row for i in range(others.column)]
        if self.row == 0 or self.row == 0:
            print('矩阵不得为空')
            raise NameError
        elif self.column != others.row:
            print('矩阵格式不匹配')
            raise NameError
        for i in range(self.row):
            for j in range(others.column):
                for k in range(self.column):
                    result_value[i][j] += self.matrix[i][k] * others.matrix[k][j]
        return result_value


if __name__ == '__main__':
    m1 = Matrix([[2, 1, 6],
                 [4, 3, 2]])
    m2 = Matrix([[1, 2],
                 [1, 0],
                 [2, 1]])
    result = m1.matrix_multiplication(m2)
    print(result)





