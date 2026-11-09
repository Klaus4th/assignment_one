def solution(A,K):
  if len(A) == 0:
    return A
  c = [0]*len(A)
  if K >= len(A):
    while K >= len(A):
      K -= len(A)
  for i, x in enumerate(A):
    if i+K < len(A):
      c[i+K] = A[i]
    else:
      c[i+K-len(A)] = A[i]
  return c
