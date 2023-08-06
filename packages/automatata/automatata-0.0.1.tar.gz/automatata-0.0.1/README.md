# automatata

Automata in Python!

## Usage

Here's a Discrete Finite Automaton that accepts words that contain an even number of "a"s and "b"s.

```python
from automatata.models.dfa import DFA

evens = DFA(
    language={"a", "b"},
    edges={
        0: {
            "a": 1,
            "b": 1,
        },
        1: {
            "a": 0,
            "b": 0,
        },
    },
    start=0,
    goal={0},
)

assert evens.valid("")
assert not evens.valid("a")
assert evens.valid("ab")
assert evens.valid("ba")
assert not evens.valid("aba")
assert not evens.valid("aab")
assert not evens.valid("abb")
for i in range(10):
    for p in permutations("a"*i + "b"+i):
        assert evens.valid(p)
assert evens.valid("aaaabb")
```
