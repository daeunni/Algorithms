# Useful functions 

1. 2차원 리스트를 왼쪽으로 90도 회전하는 함수

'''
def rotate_matrix_90degree(a):
    n = len(a)
    m = len(a[0])
    result = [[0] * n for _ in range(m)]      
    for i in range(n):
        for j in range(m):
            result[j][n-i-1] = a[i][j]
    return result
'''
