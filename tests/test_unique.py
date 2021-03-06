from sorted import deduplicate_sorted_iterable, Sorted


def test_empty():
    assert list(deduplicate_sorted_iterable(iter([]))) == []


def test_deduplicate_no_key():
    i = deduplicate_sorted_iterable(iter([1, 2, 2, 3, 4, 4]))
    assert list(i) == [1, 2, 3, 4]


def test_deduplicate_with_key():
    i = deduplicate_sorted_iterable(
        iter([1, -2, 2, -3, 4, -4]),
        key=abs
    )
    assert list(i) == [1, -2, -3, 4]


def test_unique():
    s = Sorted([1, 2, 2, 3])
    assert list(s.unique()) == [1, 2, 3]
