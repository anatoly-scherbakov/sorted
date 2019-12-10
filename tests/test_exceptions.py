from sorted import KeyFunctionMismatchError, Sorted, DirectionMismatchError


def test_key_mismatch_error():
    err = KeyFunctionMismatchError(
        Sorted([1, 2, 3]),
        Sorted(['a', 'b', 'c'], key=len)
    )

    assert str(err).startswith('Given 2 iterables are incompatible')


def test_reserve_mismatch_error():
    err = DirectionMismatchError(
        Sorted([1, 2, 3]),
        Sorted(['c', 'b', 'a'], reverse=True),
        Sorted([4, 5, 6])
    )

    assert str(err).startswith('Given 3 iterables are incompatible')
