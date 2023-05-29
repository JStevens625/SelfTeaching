matrix = [[0,5,0,2,0],[3,0,1,0,0],[0,7,0,0,4],[4,0,0,8,0]]

def maxCoin(matrix):
    maxamount = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if(i-1 or j-1 < 0):
                continue
            else:
                if matrix[i-1][j] > matrix[i][j-1]:
                    maxamount += matrix[i-1][j]
                else:
                    maxamount += matrix[i][j-1]
    print(maxamount)

def main():
    maxCoin(matrix)

main()
