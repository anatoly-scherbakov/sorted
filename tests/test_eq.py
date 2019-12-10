import itertools

from sorted import Sorted


def test_empty():
    assert Sorted([]) == Sorted([])


def test_wrong_direction():
    assert Sorted([]) != Sorted([], reverse=True)


def test_wrong_key():
    assert Sorted([]) != Sorted([], key=abs)


def test_wrong_iterable():
    assert Sorted(range(100)) != Sorted(itertools.count())


def test_all_set():
    iterable = itertools.count()
    assert Sorted(iterable) == Sorted(iterable)
