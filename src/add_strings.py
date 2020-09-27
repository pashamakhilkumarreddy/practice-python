def add_strings(num1: str, num2: str) -> str:
  return str(eval(num1) + eval(num2))

def add_strings_two(num1: str, num2:str) -> str:
  n1, n2 = 0, 0
  m1, m2 = 10 ** (len(num1) - 1), 10 ** (len(num2) - 1)
  for i in num1:
    n1 += (ord(i) - ord('0')) * m1
    m1 = m1//10
  for j in num2:
    n2 += (ord(j) - ord('0')) * m2
    m2 = m2//10
  return str(n1 + n2)

print(add_strings('12', '13'))

print(add_strings_two('121', '131'))