from permutation import *
from simplesort import *

def test_permute():
    assert sorted(permute('hat')) == ['aht','ath','hat','hta','tah','tha']


def test_sorting():
    assert simplesort('70.920 -38.797 14.354 99.323 90.374 7.581') == '-38.797 7.581 14.354 70.920 90.374 99.323'
