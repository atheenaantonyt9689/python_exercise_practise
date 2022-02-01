# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#


def diagonalDifference(arr):

    # Write your code here
    dia1 = []
    dia2 = []

    for i in range(n):
        row_length = len(arr[i])
        for j in range(row_length):
            if arr[i] == arr[j]:
                diagonal_elemnt = arr[i][j]
                dia1.append(diagonal_elemnt)

    for p in range(n):
        for q in range(len(arr[p])):
            if p + q == (n - 1):
                second_diag = arr[p][q]
                dia2.append(second_diag)

    result = abs(sum(dia1) - sum(dia2))
    return result


if __name__ == "__main__":
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input("n :").strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input("enter the elements  :").rstrip().split())))
    result = diagonalDifference(arr)
    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
