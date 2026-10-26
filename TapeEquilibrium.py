def solution(A):
    LeftSide = 0
    RightSide = sum(A)
    def checkDiff():
        return abs(LeftSide - RightSide)
    #convinent subfunction that checks the actual value of each split
    SmallestDiff = None
    for x in range(len(A) - 1):
        #This function iterates through all of the possible solutions and see which is smallest
        LeftSide = LeftSide + A[x]
        RightSide = RightSide - A[x]
        if SmallestDiff is None or SmallestDiff > checkDiff():
            SmallestDiff = checkDiff()
    return SmallestDiff