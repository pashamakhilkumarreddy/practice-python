from typing import List

def move_zeros(arr: List[int]) -> List[int]:
  for i in arr:
    if i == 0:
      arr.remove(i)
      arr.append(i)
  return arr

print(move_zeros([10, 7, 0, 0, 34, 22, 91, 100, 121]))
print(move_zeros([9, 34, 45, 62, 0, 0, 11, 0, 83, 59, 0]))