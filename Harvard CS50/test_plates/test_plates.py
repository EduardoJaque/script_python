from plates import is_valid
def test_cs50():
    assert is_valid("CS50")==True
def test_cs50():
    assert is_valid("S50")==False
def test_PI314():
    assert is_valid("PI3.14")==False
def test_CS50P2():
    assert is_valid("CS50P2")==False
def test_NRVOUS():
    assert is_valid("NRVOUS")==True
def test_OUTATIME():
    assert is_valid("OUTATIME")==False
def test_ECTO88():
    assert is_valid("ECTO88")==True

def test_CS05():
    assert is_valid("CS052")==False
def test_H():
    assert is_valid("H")==False





