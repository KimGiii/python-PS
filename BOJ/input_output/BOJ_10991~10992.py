# 10991번
# n = int(input())
#
# for i in range(1, n+1):
#     print(' '*(n-i) + '* '*i)

# 10992번
n = int(input())
for i in range(1, n+1):
    if i == 1:
        print(' '*(n-i) + '*')
    elif 1 <= i <= n-1:
        print(' '*(n-i) + '*' + ' '*(2*i-3) + '*')
    else:
        print('*'*(2*i-1))