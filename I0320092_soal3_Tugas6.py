
for y in range (10,25):
    if y == 1:
        print(y, "bukan bilangan prima")
    elif y == 2:
        print(y, "bilangan prima")
    else:
        for n in range (2, y):
            if y % n == 0:
                print(y, "bukan bilangan prima")
                break
        else:
            print(y, "bilangan prima")
