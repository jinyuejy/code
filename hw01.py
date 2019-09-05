for i in range (1,10):
    for j in range(1,10):
        if j<i:
            print(8*' ',end=' ')
        else:
            print(f"{i:2d}x{j:<2d}={i*j:2d}",end=' ')
    print(' ')