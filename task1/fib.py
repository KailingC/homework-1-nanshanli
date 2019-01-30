def fib(n):
  prev = 1
  curr = 1

  if n == 1:
    return 1
  elif n == 2:
    return 1

  for i in range(3, n + 1):
    temp = prev + curr
    prev = curr
    curr = temp

  return curr
