# n = 3
# m = 4
# mat = [0] * n
# for i in range(n):
#     mat[i] = [0] * m
# print('Matrice (', n, 'x', m, '):')
# for i in range(n):
#     print(mat[i], end=' ')
#     print()

n = int(input("Nr de linii: "))
m = int(input("Nr de coloane: "))
# mat = [[0 for j in range(m)] for i in range(n)]
# print('matrice(', n, 'x', m, '):')
# for i in range(n):
#     print(*mat[i], end=' ')
#     print()
# mat = [[0 for i in range(m)] for i in range(n)]
mat = [[int(j) for j in input(f"dati elem de pe linia: [{i+1}]=").split()] for i in range(n)]
for linie in mat:
    print(linie)
