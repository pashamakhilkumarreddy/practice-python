from typing import List, Any

def fill_in_the_blanks(arr: List[Any]) -> List[Any]:
  res: List[Any] = [] 
  valid: Any = 0
  for i in arr:
    if i != None:
      res.append(i)
      valid = i
    else:
      res.append(valid)
  return res

print(fill_in_the_blanks([1, 100, None, 23, None, 45, None, None, 76, 84, 99, None]))