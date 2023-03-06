from LinearMatrix.Matrix import Matrix


def main():
    myMatrix = Matrix()
    eqs = [
        "4x-3y-2z=5",
        "-2x-y-z=-4",
        "-7x-5y-7z=-31"
    ]
    myMatrix.from_system_strings(eqs, 3)
    print(myMatrix.solve())


if __name__ == "__main__":
    main()
