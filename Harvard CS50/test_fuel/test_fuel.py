import pytest
from fuel import convert, gauge
def test_34():
    assert convert("3/4")==75.0
def test_75():
    assert gauge(75)=="75%"
def test_13():
    assert convert("1/3")==33
def test_33():
    assert gauge(33)=="33%"
def test_0100():
    assert convert("0/100")==0
def test_0():
    assert gauge(0)=="E"
def test_99():
    assert convert("99/100")==99
def test_99():
    assert gauge(99)=="F"
def test_1():
    assert convert("1/100")==1
def test_1():
    assert gauge(1)=="E"
def test_ValueError():
    with pytest.raises(ValueError):
        convert("4/1")
def test_ZeroDivisionError():
    with pytest.raises(ZeroDivisionError):
        convert("0/0")