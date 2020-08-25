def reverse_integer(number: int) -> str:
  string = str(number)
  if string[0] == '-':
    return int('-' + string[:0:-1]
  return int(string[:0:-1])
  
