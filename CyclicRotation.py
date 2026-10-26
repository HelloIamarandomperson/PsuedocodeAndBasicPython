def solution(A,k):
    if len(A) == 0:
        return A
    newArray = [None]*len(A)
    #newArray will be the finished array with everything in the proper location
    for x in range(len(A)):
        shift = x + k
        while shift >= len(A):
            shift = shift - len(A)
        newArray[shift] = A[x]

    return newArray
