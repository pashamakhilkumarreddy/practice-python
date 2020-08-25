from typing import List

def check_prime(length: int) -> List[int]:
  # type (int) -> List[int]
  prime_numbers = []
  for num in range(length):
    if num > 1:
      for i in range(2, num):
        if num % i == 0:
          break
      else:
        prime_numbers.append(num)
  return prime_numbers
  
  
print(check_prime(10))