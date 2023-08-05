def createMatrix(row, col, dataList):   
    mat = []
    for i in range (row):
        rowList=[]
        for j in range (col):
            rowList.append(dataList[col*i+j])
        mat.append(rowList)
    return mat

def printMatrix(matrix):
    for i in matrix:
        print(i)

def matSum(*mat):
    C=[]
    for r in range(len(mat[0])):
        rowList=[]
        for c in range(len(mat[0][0])):
            Sum=0
            for m in range(len(mat)):
                Sum=Sum+mat[m][r][c]
            rowList.append(Sum)
        C.append(rowList)
    return C

def matMin(*mat):
    C=[]
    for r in range(len(mat[0])):
        rowList=[]
        for c in range(len(mat[0][0])):
            Sum=mat[0][r][c]
            for m in range(1,len(mat)):
                Sum=Sum-mat[m][r][c]
            rowList.append(Sum)
        C.append(rowList)
    return C

def matMul(mat1, mat2):
    C=[]
    for r in range(len(mat1)):
        rowList=[]
        for c in range(len(mat2[0])):
            Sum=0
            for i in range(len(mat1[0])):
                Sum=Sum+mat1[r][i]*mat2[i][c]
            rowList.append(Sum)
        C.append(rowList)
    return C