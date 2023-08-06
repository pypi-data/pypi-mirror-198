from itertools import permutations

from automatata.models.dfa import DFA


def test_dfa_model():
    dfa = DFA(
        language={"a", "b"},
        edges={0: {"a": 0, "b": 1}, 1: {}},
        start=0,
        goal={1},
    )
    assert dfa.language == {"a", "b"}
    assert dfa.states == {0, 1}
    assert dfa.start == 0
    assert dfa.goal == {1}


def test_one_or_mode_a_and_one_b():
    as_and_one_b = DFA(
        language={"a", "b"},
        edges={0: {"a": 0, "b": 1}, 1: {}},
        start=0,
        goal={1},
    )

    assert not as_and_one_b.valid("")
    assert not as_and_one_b.valid("a")
    assert not as_and_one_b.valid("aaaaaaaaaaaa")
    assert as_and_one_b.valid("ab")
    assert as_and_one_b.valid("aaaaaaaaaaab")


def test_even_as_and_bs():
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
    for i in range(6):
        for p in permutations("a" * i + "b" * i):
            assert evens.valid(p)
    assert evens.valid("aaaabb")
