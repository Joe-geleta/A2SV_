def countSwaps(a):
    n = len(a)
    swaps = 0
    for i in range(n-1):
        for j in range(n-i-1):
            if (a[j] > a[j+1]):
                a[j],a[j+1] = a[j+1],a[j]
                swaps += 1
    print("Array is sorted in {} swaps.".format(swaps))
    print("First Element: {}".format(a[0]))
    print("Last Element: {}".format(a[n-1]))

    return countSwaps
