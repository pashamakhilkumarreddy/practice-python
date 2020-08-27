from __future__ import annotations
from collections import (namedtuple, deque, Counter, OrderedDict, defaultdict, ChainMap)
from typing import (
  NamedTuple, List, Deque, Any, 
  Counter as CounterT, DefaultDict as DefaultDictT,
  ChainMap as ChainMapT,
  MutableMapping,
  Dict
)

RGBColor = NamedTuple('color',[('red', int), ('green', int), ('blue', int)])

"""
Named Tuple
"""
def rgb(r : int, g : int, b : int) -> RGBColor:
  return RGBColor(red = r, green = g, blue = b)

result = rgb(110, 143, 212)
print(f'Red {result.red}')
print(f'Green {result.green}')
print(f'Blue {result.blue}')

"""
Deque
"""
def dequeEx(names: List[str]) -> Deque[str]:
  deq: Deque[str] = deque(names)
  deq.append('Gwen Stacy')
  deq.appendleft('Ashido Kano')
  # dep.pop()
  # dep.popleft()
  return deq

que = dequeEx(['Raizo', 'Kaylene'])
print(f'Queue {que}')

"""
Counter
"""
def counterEx(ele: List[Any]) -> CounterT:
  return Counter(ele)

count = counterEx(['a','b','a','c','b','b','d', 'f', 'd', 'a', 'g', 'b', 'c', 'd'])
print(f'{count}')
print(f'Most common {count.most_common(1)}')
print(f'Elements {list(count.elements())}')

"""
Ordered Dict
"""
def orderedDictEx() -> MutableMapping[str, int]:
  od: MutableMapping[str, int] = OrderedDict()
  od['a'] = 1
  od['b'] = 2
  od['c'] = 3
  od.update({'d' : 4, 'e': 5})
  return od

print(f'OrderedDict Ex: ${orderedDictEx()}')

"""
Default Dict
"""
def defaultDictEx() -> DefaultDictT:
  dd: DefaultDictT = defaultdict(int)
  dd['a'] = 1
  dd['b'] = 2
  dd['c'] = 3
  _ = dd['d']
  return dd

print(f'DefaultDict {defaultDictEx()}')

"""
Chain Map
"""
def chainMapEx() -> ChainMapT[str, int]:
  dict_1 = { 'a' : 1, 'b' : 2 }
  dict_2 = { 'c' : 3, 'd' : 4 }
  chain_map: ChainMapT[str, int] = ChainMap(dict_1, dict_2)
  return chain_map

print(f'Chain Map: {chainMapEx()}')