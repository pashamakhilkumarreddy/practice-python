from typing import List

def monotonic_array(arr: List[int]) -> bool:
  return (all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1)) 
          or all(arr[i] >= arr[i + 1] for i in range(len(arr) - 1)))

print(monotonic_array([1, 2, 3, 4, 5, 6, 7, 8, 91]))
print(monotonic_array([11, 2, 32, 41, 25, 16, 17, 5, 8]))
print(monotonic_array([9, 8, 7, 6, 5, 4, 3, 2, 1]))