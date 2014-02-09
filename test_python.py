from permutation import *

def test_permute():
    assert sorted(permute('hat')) == ['aht','ath','hat','hta','tah','tha']
