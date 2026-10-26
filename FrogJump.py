def solution(x,y,d):
    while x < y:
      #function originally iterated jumps until x is over or equal to y, but claude told me that was gonna be too slow, so instead the function removes x from y, and then rounds up y/d, sorry that it doesn't match the pseudocode?
      y=y-x
      y=(y-1+d)//d
    return y