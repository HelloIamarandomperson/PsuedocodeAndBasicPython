def solution(A):
    #this function finds a the element which is stopping this array from being a permutation, and outputs it's location in the original array
    sortedA = sorted(A)
    for x in range(len(sortedA)):
        #Since the array is sorted, if any of them don't correspond to their position, that means they are missing
        if sortedA[x] != x+1:
            location = A.index[x+1]
            return location