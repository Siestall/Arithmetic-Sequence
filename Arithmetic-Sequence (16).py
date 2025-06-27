try:
    n1 = int(input('Num 1: '))
    n2 = int(input('Num 2: '))
    n3 = int(input('Num 3: '))
    if (n1 - n2) == (n2 - n3):
        print('The numbers ARE three consecutive elements of an arithmetic sequence')
    else:
        print('The numbers ARE NOT three consecutive elements of an arithmetic sequence')
except:
    print('Enter integer')