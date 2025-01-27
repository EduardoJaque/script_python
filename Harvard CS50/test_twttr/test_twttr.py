from twttr import shorten
def test_prueba():
    assert shorten("jake")=="jk"
def test_prueba2():
    assert shorten("JAKE")=="JK"
def test_numero():
    assert shorten("10")=="10"
def test_punto():
    assert shorten(".,.,")==".,.,"
if __name__ == "__main__":
    test_prueba()
    test_prueba2()
    test_numero()
    test_punto()