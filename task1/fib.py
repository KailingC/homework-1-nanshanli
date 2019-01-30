def fib(n):
  prev = 1
  curr = 1
  
  if n == 1:
    return 1
  else if n == 2:
    return 1
    
  for i in range(3, n):
    temp = prev + curr
    prev = curr
    curr = temp
    
  return curr
    
