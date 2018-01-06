def bounce(n):
    if n !=0:
        print n,
        bounce(n-1)
        print n,
        return
    else:
        print n,


def bounce2(n):
    c=n
    while n != 0:
        print n,
        n=n-1

    while n!=c:
        print n,
        n=n+1
    else:
        print n



