from LinearMatrix import Matrix


def main():
    myMatrix = Matrix()
    myMatrix.set_matrix([
        [5, 1],
        [2, 2],
        [4, 1]
    ])
    myMatrix2 = Matrix([
        [0, 0],
        [0, 0]
    ])
    print(myMatrix * myMatrix2)


if __name__ == "__main__":
    main()
