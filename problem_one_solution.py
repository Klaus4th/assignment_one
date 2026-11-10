def solution(A,K):
  if len(A) == 0:
    return A
  # if the list is empty, we return the empty list
  c = [0]*len(A)
  # we create an empty list, this will be the list we return as we are remaking the list
  if K >= len(A):
    #if the amount we're shifting the list is longer than the list, we remove the length of the list from that amount
    # until the amount is less than the lists length, we will save this number
    while K >= len(A):
      K -= len(A)
      
  for i, x in enumerate(A):
    if i+K < len(A):
      c[i+K] = A[i]
      #if i+k is within the length of the list we can use that as an index
    # if not we subtract the length of the list like below V
    else:
      c[i+K-len(A)] = A[i]
  return c
