def utopianTree(n):
    boolean = False
    count=0
    for i in range(n+1):
        if(boolean == False):
            count+=1
            boolean = True
        else:
            count*=2
            boolean=False
    return count
