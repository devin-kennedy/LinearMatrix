from .utils import *


class Matrix(object):
    def __init__(self, matrix=None):
        self.matrix = self.set_matrix(matrix) if matrix else []

        self.numOfTerms = None

    def __str__(self):
        out = ""
        for row in self.matrix:
            out += str(row) + "\n"
        return out

    def __len__(self):
        return len(self.matrix)

    def __getitem__(self, item):
        return self.matrix[item]

    def __setitem__(self, key, value):
        self.matrix[key] = value

    def __mul__(self, other):
        if type(other) == int or type(other) == float:
            return [[i * other for i in row] for row in self.matrix]
        if self.shape()[0] != other.shape()[1]:
            raise ValueError("Cannot multiply these matricies")
        if type(other) == Matrix:
            out_matrix = Matrix()
            out_matrix.zeros((self.shape()[0], other.shape()[1]))

            for i in range(self.shape()[0]):
                for j in range(other.shape()[1]):
                    mulRow = self[i]
                    mulCol = other.get_col(j)
                    out_matrix[i][j] = dot_product(mulRow, mulCol)
            return out_matrix
        else:
            raise ValueError(f"Cannot multiply type {type(other)} by Matrix")

    def __iter__(self):
        for row in self.matrix:
            yield row
    
    def __add__(self, other):
        if type(other) != Matrix:
            raise ValueError(f"Cannot add type {type(other)} and Matrix")
        if other.shape() != self.shape():
            raise ValueError("Cannot add two matricies of different shapes")
        return [[self[i][j] + other[i][j] for j in range(len(self[i]))] for i in range(len(self))]

    def __sub__(self, other):
        if type(other) != Matrix:
            raise ValueError(f"Cannot subtract type {type(other)} and Matrix")
        if other.shape() != self.shape():
            raise ValueError("Cannot subtract two matricies of different shapes")
        return [[self[i][j] - other[i][j] for j in range(len(self[i]))] for i in range(len(self))]

    def set_matrix(self, newMatrix):
        self.matrix = newMatrix
        if not self.__verify_shape_integrity():
            raise ValueError("Invalid matrix given")
        self.numOfTerms = self.shape()[1]

    def zeros(self, shape: tuple):
        self.set_matrix([[0 for _ in range(shape[1])] for _ in range(shape[0])])

    def get_col(self, i):
        return [row[i] for row in self]

    def shape(self):
        return len(self), len(self[0])

    def __verify_shape_integrity(self):
        allLens = [len(row) for row in self]
        return all_equal(allLens)

    def is_initialized(self):
        if self.matrix != [] and self.numOfTerms is not None and self.__verify_shape_integrity():
            return True
        return False

    def from_system_input(self, numOfTerms):
        eqs = numOfTerms

        system = []
        for i in range(1, eqs + 1):
            eq = input_to_linEq(input(f"({i}/{eqs}) Enter a linear equation with {numOfTerms} terms: "))
            while len(eq[0]) > numOfTerms:
                print("Incorrect number of terms inputted")
                eq = input_to_linEq(input(f"({i}/{eqs}) Enter a linear equation with {numOfTerms} terms: "))
            system.append(eq)

        self.set_matrix(system_toMatrix(system))

    def from_system_strings(self, systemStrs, numOfTerms):
        system = []
        for str_eq in systemStrs:
            eq = input_to_linEq(str_eq)
            if len(eq[0]) > numOfTerms:
                raise ValueError("More terms than terms declared")
            system.append(eq)
        self.set_matrix(system_toMatrix(system))

    def is_reduced(self):
        for i in range(len(self)):
            if self[i][i] != 1:
                return False
            if sum(self[i][0:i]) and i != 0:
                return False
        return True

    def interchange_row(self, i, j):
        if i == j:
            raise ValueError("Cannot interchange the same row")

        row_i = self[i]
        row_j = self[j]
        self[i] = row_j
        self[j] = row_i

    def mul_row(self, cst, row_i):
        if len(self) - 1 < row_i:
            raise ValueError("Index not in matrix")

        temp_row = []
        for i in range(len(self[row_i])):
            temp_row.append(self[row_i][i] * cst)

        self[row_i] = normalize_floats_row(temp_row)

    def mul_row_add(self, cst, mulRow, addRow):
        if mulRow == addRow:
            raise ValueError("Cannot multiply and add to the same row")

        temp_row = []
        for i in range(len(self[addRow])):
            temp_row.append((cst * self[mulRow][i]) + self[addRow][i])

        self[addRow] = normalize_floats_row(temp_row)

    def reduce(self):
        if self[0][0] != 1:
            for i in range(1, len(self)):
                if self[i][0] == 1:
                    self.interchange_row(0, i)
                    break
        if self[0][0] != 1:
            self.mul_row((1 / self[0][0]), 0)

        for i in range(1, len(self)):
            if sum(self[i][0:i]) != 0:
                for j in range(len(self[i][0:i])):
                    if self[i][0:i][j] != 0:
                        self.mul_row_add(-(self[i][0:i][j]), j, i)
            if self[i][i] != 1:
                self.mul_row((1 / self[i][i]), i)

    def solve_system(self):
        if not self.is_reduced():
            self.reduce()

        systemVars = [self[-1][-1]]

        for i in range(len(self) - 2, -1, -1):
            row = self[i]
            to_alge = row[i + 1:-1]
            left_alge = sum([
                to_alge[i] * list(reversed(systemVars))[i] for i in range(len(to_alge))
            ])
            systemVars.append(row[-1] - left_alge)

        return normalize_floats_row(list(reversed(systemVars)))

