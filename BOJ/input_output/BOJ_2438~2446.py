"""2438"""
# n = int(input())
#
# for i in range(1, n+1):
#     s = '*'
#     print(s*i)

"""2439"""

# for i in range(1, n+1):
#     s = '*'
#     b = ' '
#     print(b*(n-i) + s*i)

"""2440"""

# for i in range(n):
#     s = '*'
#     print(s*(n-i))

# for i in range(n, 0, -1):
#     s = '*'
#     print(s*i)

"""2441"""
# for i in range(n):
#     print(' '*i + '*'*(n-i))

"""2442"""
# for i in range(1, n+1):
#     print(' '*(n-i) + '*'*(2*i-1))

"""2445"""
# for i in range(1, 2*n):
#     if i <= n:
#         print('*'*i + ' '*2*(n-i) + '*'*i)
#     else:
#         print('*'*(2*n-i) + ' '*2*(i-n) + '*'*(2*n-i))

"""2446"""
n = int(input())
for i in range(1, 2*n):
    if i <= n:
        print(' '*(i-1) + '*'*(2*(n-i)+1))
    else:
        print(' '*(2*n-i-1) + '*'*(2*(i-n)+1))