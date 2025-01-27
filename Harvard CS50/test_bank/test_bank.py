from bank import value

def test_hello():
    assert value("hello")==0
def test_Hello_Newman():
    assert value("Hello, Newman")==0
def test_How_you_doing():
    assert value("How you doing")==20
def test_What_s_happening():
    assert value("What's happening")==100
def test_What_s_up():
    assert value("What's up")==100