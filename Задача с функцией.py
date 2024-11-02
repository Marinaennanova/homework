def get_matrix (n,m,value):
    matrix = []
    for i in range (n):
        for j in range (m):
         str = [value]
         matrix.append(str)
         stolb = [value]
         matrix.append(stolb)
    
    return matrix
        
result1 = get_matrix(1,2,0)
result2 = get_matrix(3,5,1)
result3 = get_matrix(1,2,3)
print(result1)
print(result2)
print(result3)

