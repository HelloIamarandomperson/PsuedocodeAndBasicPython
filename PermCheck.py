def solution(A):
    sortedA = sorted(A)
    #ordering the array so the index position is the same as it's value means we don't have to keep track of the past loop in the for loop
    for x in range(len(sortedA)):
        #Since the array is sorted, if any of them don't correspond to their position, that means they are missing
        if sortedA[x] != x+1:
            return 0
    return 1