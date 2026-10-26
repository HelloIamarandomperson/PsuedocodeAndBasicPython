def solution(A):
    sortedA = sorted(A)
    for x in range(len(sortedA)):
        #Since the array is sorted, if any of them don't correspond to their position, that means they are missing
        if sortedA[x] != x+1:
            return x+1