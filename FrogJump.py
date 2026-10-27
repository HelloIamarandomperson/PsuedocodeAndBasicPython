def solution(x,y,d):
    jumps = 0
    while x < y:
      #function iterates jumps until x is over or equal to y, simple enough
      x=x+d
      jumps=jumps+1
    return jumps