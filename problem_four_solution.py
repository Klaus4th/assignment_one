def solution(A):
    n = len(A)
  # one must check to see if the array length is 0, that would mean we must return one
    if n == 0:
        return 1
      # will iterate through all of the numbers 0-n-1
    for i in range(n):
        if A.count(i+1) == 0:
            return i+1
          # we check if a number doesn't occur in 1-n and return that number if so
    return n+1
  # if not we return n+1 as it is the last number in the list that is missing
