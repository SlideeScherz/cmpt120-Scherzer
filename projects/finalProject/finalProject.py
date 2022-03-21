num = 5

for i in range(num):
    for j in range(num):
        if (i == j) or ((num - j - 1) == i):
            print('*', end='')
        else:
            print(' ', end='')
    print('')
