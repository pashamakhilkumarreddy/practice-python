def avg_word_len(sentence: str) -> float:
  if not sentence or not sentence.strip():
    print("Can't find length of any empty string")
    return -1
  for p in '!?",;.:':
    sentence = sentence.replace(p, '')
  words = sentence.split()
  return round(sum(len(word) for word in words) / len(words), 2)

print(avg_word_len('Ich liebe dich: Gwen Stacy'))