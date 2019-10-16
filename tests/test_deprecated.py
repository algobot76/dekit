import warnings

from dekit import deprecated


def test_deprecated():
    @deprecated
    def foo():
        return 'foo'

    with warnings.catch_warnings(record=True) as w:
        warnings.simplefilter("always")
        foo()
        assert len(w) == 1
        assert w[0].message == 'This method has been deprecated'
