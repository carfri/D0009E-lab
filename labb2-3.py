def suman(n):
    if n>0:
        return n%10+suman(n/10)
    else:
        return 0

