import math

import LinearMatrix.Matrix


def has_numbers(string):
    return any(char.isdigit() for char in string)


def input_to_linEq(usr_in):
        lrParsed = usr_in.split("=")
        eq_right = int(lrParsed[1])
        eq_left = lrParsed[0]

        if list(eq_left)[0] != "-":
            terms = eq_left.replace("-", "+-").split("+")
        else:
            terms = ("-" + eq_left[1:].replace("-", "+-")).split("+")

        allTerms = []
        for t in terms:
            term = {"mul": None, "id": None}
            if not has_numbers(t):
                if list(t)[0] != "-":
                    term["id"] = t
                    term["mul"] = 1
                else:
                    term["id"] = t.replace("-", "")
                    term["mul"] = -1
            else:
                termChars = list(t)
                idChars = []
                isNeg = False
                for c in range(len(termChars)):
                    try:
                        if not termChars[c].isdigit():
                            if termChars[c] == "-":
                                isNeg = True
                            else:
                                idChars.append(termChars[c])
                            termChars.pop(c)
                    except IndexError:
                        pass
                mul = int("".join(termChars))
                if isNeg:
                    mul *= -1

                term["id"] = "".join(idChars)
                term["mul"] = mul

            allTerms.append(term)
        return allTerms, eq_right


def linEq_toStr(linEq):
    terms = linEq[0]
    terms_out = []
    for t in terms:
        tout = ""
        for k, v in t.items():
            if v:
                tout += str(v)
        terms_out.append(tout)

    return " + ".join(terms_out) + " = " + str(linEq[1])


def system_toMatrix(system):
    matrix = []
    for eq in system:
        row = []
        for t in eq[0]:
            row.append(t["mul"])
        row.append(eq[1])
        matrix.append(row)

    matrix = normalize_floats(matrix)
    return matrix


def normalize_floats(matrix):
    for i in range(len(matrix)):
        matrix[i] = normalize_floats_row(matrix[i])
    return matrix


def normalize_floats_row(row):
    for i in range(len(row)):
        e = row[i]
        if type(e) == float:
            if math.modf(e)[0] == 0.0:
                e = int(e)
        row[i] = e
    return row


def dot_product(tup1, tup2):
    zipped = list(zip(tup1, tup2))
    for i in range(len(zipped)):
        zipped[i] = zipped[i][0] * zipped[i][1]
    return sum(zipped)


def all_equal(lst):
    return len(set(lst)) <= 1


def det_simple(matrix):
    if type(matrix) != LinearMatrix.Matrix.Matrix:
        raise ValueError("Must give a Matrix object")

    if matrix.shape() != (2, 2):
        raise ValueError("Function requires a 2x2 Matrix object")

    return (matrix[0][0] * matrix[1][1]) - (matrix[0][1] * matrix[1][0])


def is_even(num):
    if num % 2 == 0:
        return True
    return False
