from time import time
import timeit

def time_test():
  start = time()
  end = time()
  print(f'Execution time is {end - start}')
  
time_test()

def timeit_test():
  time = timeit.timeit(stmt = 'sum(sqrt(x) for x in range(1, 10000))',
                       setup = 'from math import sqrt', number = 10)
  print(f'Execution time is {time}')
  
timeit_test()