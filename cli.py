import sys
import csv
import math

def isSquareMatrix(table) -> bool:
    '''
    Function to check if the elements of a given table form a square matrix.

    Parameter(s):
        table(list) : Matrix Table in the form [X, X, X, X, X, X]

    Returns:
        True(bool) : If given table is Square Matrix
        False(bool) : Otherwise
    '''
    square_root = int(math.sqrt(len(table)))
    return len(table) == square_root**2


def matrixify(table) -> list:
    '''
    Function to convert the Table to Matrix form:

    Parameter(s):
        table(list) : Matrix Table in the form [X, X, X, X, X, X]

    Returns:
        matrix(list) : Matrix Table in the form [[X, X], [X, X], [X, X]]
    '''
    square_root = int(math.sqrt(len(table)))
    matrix = []
    row = []
    for index, value in enumerate(table):
        row.append(value)
        if index%square_root==(square_root-1):
            matrix.append(row)
            row=[]

    return matrix

def dematrixify(matrix) -> list:
    '''
    Function to convert the Matrix to Table form.

    Parameter(s):
        table(list) : Matrix Table in the form [X, X, X, X, X, X]

    Returns:
        matrix(list) : Matrix Table in the form [[X, X], [X, X], [X, X]]
    '''
    table = []
    for row in matrix:
        for num in row:
            table.append(num)

    return table


def rotateTable(table) -> list:
    '''
    Function to right rotate the Matrix by 1

    Parameter(s):
        table(list): Matrix Table in the form [X, X, X, X]

    Returns:
        (list) : Returns the right rotated Matrix
    '''
    matrix = matrixify(table)

    top = left = 0
    bottom = right = len(matrix)-1
 
    while left < right and top < bottom:
 
        # Store the first element of next row,
        # this element will replace first element of
        # current row
        previous = matrix[top+1][left]
 
        # Move elements of top row one step right
        for i in range(left, right+1):
            current = matrix[top][i]
            matrix[top][i] = previous
            previous = current
 
        top += 1
 
        # Move elements of rightmost column one step downwards
        for i in range(top, bottom+1):
            current = matrix[i][right]
            matrix[i][right] = previous
            previous = current
 
        right -= 1
 
        # Move elements of bottom row one step left
        for i in range(right, left-1, -1):
            current = matrix[bottom][i]
            matrix[bottom][i] = previous
            previous = current
 
        bottom -= 1
 
        # Move elements of leftmost column one step upwards
        for i in range(bottom, top-1, -1):
            current = matrix[i][left]
            matrix[i][left] = previous
            previous = current
 
        left += 1
    
    return dematrixify(matrix)

def main():
    '''
    Main method.
    '''
    # CLI arguments
    inFile = sys.argv[1]
    outFile = sys.argv[2]    

    fields = []

    with open(inFile, 'r') as csvFileIn, open(outFile, 'w', newline='') as csvFileOut:

        csvReader = csv.reader(csvFileIn)
        csvWriter = csv.writer(csvFileOut)
        
        # Updating the fields of Output file
        fields = next(csvReader)
        fields.append("is_valid")
        csvWriter.writerow(fields)

        # Running the main logic for each row in CSV file
        for row in csvReader:
            id = row[0]
            table = None

            #Converting Table in type(str) to type(list)
            if row[1] and len(row[1])!=2:
                table = row[1].replace(" ","").replace("[","").replace("]","").split(",")

            if table and isSquareMatrix(table):
                rotatedTable = rotateTable(table)
                csvWriter.writerow([id, rotatedTable, True])
            else:
                csvWriter.writerow([id, [], False])
    
    
if __name__ == "__main__":
    main()