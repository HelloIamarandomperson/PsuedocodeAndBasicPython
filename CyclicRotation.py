def solution(A,k):
    #function is designed to output a array shifted by k numbers, where overflow returns to the front
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
