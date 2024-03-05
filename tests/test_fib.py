import pytest
from template_workshop import Fibonacci

def test_import():
    # This checks __init__ was set up correctly
    try:
        from template_workshop import Fibonacci
    except ImportError:
        assert False

##### YOUR CODE HERE #####
def test_fib_pos():
    fib = Fibonacci()
    assert fib.fib(0) == 0
    assert fib.fib(1) == 1
    assert fib.fib(2) == 1
    assert fib.fib(3) == 2
    assert fib.fib(6) == 8
    assert fib.fib(10) == 55
    assert fib.fib(15) == 610

def test_fib_neg():
    fib = Fibonacci()
    with pytest.raises(ValueError):
        fib.fib(-1)

def test_fib_str():
    fib = Fibonacci()
    with pytest.raises(TypeError):
        fib.fib("test")
##########################