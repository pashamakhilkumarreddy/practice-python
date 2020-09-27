def valid_palindrome(s: str) -> bool:
  for i in range(len(s)):
    t = s[:i] + s[i + 1:]
    if t == t[::-1]:
      return True
  return s == s[::-1]

print(valid_palindrome('abba'))
print(valid_palindrome('Stacy'))
print(valid_palindrome('abcba'))