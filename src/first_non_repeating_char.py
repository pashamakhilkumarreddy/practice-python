from collections import Counter

def first_non_repeating_char(s: str) -> int:
  freq = {}
  for i in s.strip():
    if i not in freq:
      freq[i] = 1
    else:
      freq[i] += 1
  for _, (k, v) in enumerate(freq.items()):
    if k.strip() and v == 1:
      return s.index(k)
  return -1

def first_non_repeating_char_sol(s: str) -> int:
  count = Counter(s.strip())
  for _, (k, v) in enumerate(count.items()):
    if k.strip() and v == 1:
      return s.index(k)
  return -1

print(first_non_repeating_char('Gwen Stacy Benjamin G'))
print(first_non_repeating_char('alphabet'))

print(first_non_repeating_char_sol('Gwen Stacy Benjamin G'))
print(first_non_repeating_char_sol('alphabet'))