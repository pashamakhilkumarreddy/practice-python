from typing import List, Tuple, Set, Any

def matched_mismatched_words(sentence_one: str, sentence_two: str) -> Tuple[List[Any], List[Any]]:
  set_one: Set[Any] = set(sentence_one.split())
  set_two: Set[Any] = set(sentence_two.split())
  return sorted(list(set_one ^ set_two)), sorted(list(set_one & set_two))

print(matched_mismatched_words('Ich liebe dich Anna', 'Es ist wichtig, Anna'))
print(matched_mismatched_words('Me encanta Anna', 'Tu eres muy importante, Anna'))