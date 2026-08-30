# *
# * *
# * * *
# * * * *
# * * * * *

# row = int(input('Input row count.\n'))
# print()

# for i in range(1, row+1, 1):
#     for j in range(0, i, 1):
#         print('* ', end='')
#     print()


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# * * * * *
# * * * *
# * * *
# * * 
# *

# row = int(input('Input row count.\n'))
# print()

# for i in range(0, row, 1):
#     for j in range(0, row-i, 1):
#         print('* ', end='')
#     print()


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# * * * * *
# * * * *
# * * *
# * *
# *

# row = int(input('Input row count.\n'))
# print()

# for i in range(1, row+1, 1):
#     for j in range(1, i, 1):        # 공백을 출력하는 부분
#         print(' ', end='')
#     for k in  range(0, (row+1)-i, 1):
#         print('* ', end='')
#     print()


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


#         *
#       * *
#     * * *
#   * * * *
# * * * * *

# row = int(input('Input row count.\n'))
# print()

# for i in range(1, row+1, 1):
#     for j in range(0, row-i, 1):    # 공백 출력부분
#         print('  ', end='')
#     for k in range(i):             # 공백을 출력한 후에 별을 출력한 부분
#         print('* ', end='')
#     print()


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


#         *
#       * * *
#     * * * * *
#   * * * * * * *
# * * * * * * * * * 

# row = int(input('Input row count.\n'))
# print()

# for i in range(1, row+1, 1):
#     for j in range(1, row+1-i, 1):
#         print('  ', end='')
#     for j in range(0, 2*i-1, 1):
#         print('* ', end='')
#     print()


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# 5         <= 키보드 입력
# 1
# 1 2
# 1 2 3 
# 1 2 3 4
# 1 2 3 4 5 

# k= 0
# row = int(input('Input row count.\n'))
# print()

# for i in range(1, row+1, 1):
#     k = 0
#     for j in range(0, i, 1):
#         k = k+1
#         print(k, end=' ')
#     print()


row = int(input('Input row count.\n'))
print()

for i in range(1, row+1, 1):
    for j in range(1, i+1, 1):
        print(j, end=' ')
    print()
