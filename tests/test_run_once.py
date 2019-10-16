from dekit import run_once


def test_run_once():
    @run_once
    def foo():
        return 'foo'

    result1 = foo()
    result2 = foo()
    assert result1 == 'foo'
    assert result2 is None
