"""Deterministic Finite Automata"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Generic, Hashable, Mapping, Sequence, TypeVar

T = TypeVar("T", bound=Hashable)

State = int


@dataclass
class DFA(Generic[T]):
    language: set[T]
    edges: Mapping[State, Mapping[T, State]]
    start: State
    goal: set[State]

    @property
    def states(self):
        return set(self.edges)

    def valid(self, word: Sequence[T]) -> bool:
        state = self.start
        for letter in word:
            state = self.edges[state][letter]
        return state in self.goal
