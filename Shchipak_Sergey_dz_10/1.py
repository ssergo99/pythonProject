class Matrix:
    mat = []

    def __init__(self, matrix):
        self.mat = matrix

    def __str__(self):
        string = ''
        for i in self.mat:
            for j in i:
                string += str(format(j, '5d')) + '     '
            string += "\n"
        self.string = string
        return self.string

    def __add__(self, other):
        fit_self_mat = list(map(list, self.mat))
        fit_other_mat = list(map(list, other.mat))
        fit_self_mat.extend([[0]] * (len(other.mat) - len(self.mat)))
        fit_other_mat.extend([[0]] * (len(self.mat) - len(other.mat)))
        for i in range(0, len(fit_self_mat)):
            fit_self_mat[i].extend([0, ] * (len(fit_other_mat[i]) - len(fit_self_mat[i])))
            fit_other_mat[i].extend([0, ] * (len(fit_self_mat[i]) - len(fit_other_mat[i])))
        for ii in range(len(fit_self_mat)):
            for jj in range(len(fit_self_mat[ii])):
                fit_self_mat[ii][jj] += fit_other_mat[ii][jj]
        return Matrix(fit_self_mat)


a = Matrix([[31, 22], [37, 43], [51, 86]])
b = Matrix([[3, 5, 32], [2, 4, 6], [-1, 64, -8]])
c = Matrix([[3, 5, 8, 3], [8, 3, 7, 1]])

print(c)
print(b)
print(c)
print(a + b)
print(a + c + b)
