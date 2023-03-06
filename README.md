# LinearMatrix
A Python Package that handles and solves matricies representing systems of linear equations

## Documentation(ish)
 - Matrix()
    Takes no init arguments
 - Matrix.from_system_input(numOfTerms)
    Takes an integer representing the number of terms expected in the linear equations
    Gets user input from console for the number of equations necessary and initializes the Matrix objects matrix
 - Matrix.from_system_string(systemStrs, numOfTerms)
    Takes a list of strings representing linear equations and an integer representing the number of terms expected in the linear equations
    Initializes the Matrix objects matrix from the given linear equations
 - Matrix.is_reduced()
    Takes no arguments
    returns a boolean representing if the matrix is in row-echelon form
 - Matrix.reduce()
    Takes no arguments
    Reduces the Matrix objects matrix to row-echelon form
 - Matrix.solve()
    Takes no arguments
    Returns a list of the values of the variables in the linear equations in the order they appear in the linear equation
 
