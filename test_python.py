from permutation import *
from simplesort import *
from findsquare import *

def tolower(abool):
    return str(abool).lower()

def test_second():
    assert tolower(issquare('(4,0), (1,4), (0,1), (4,1)')) == 'false'
    assert tolower(issquare('(2,2), (2,2), (2,2), (2,2)')) == 'false'
    assert tolower(issquare('(5,5), (3,6), (5,7), (0,1)')) == 'false'

def test_third():
    assert tolower(issquare('(7,3), (6,6), (8,5), (5,4)')) == 'true'
    assert tolower(issquare('(0,5), (2,3), (0,3), (2,5)')) == 'true'
    assert tolower(issquare('(0,1), (0,2), (1,1), (1,2)')) == 'true'

def test_fourth():
    assert tolower(issquare('(5,9), (4,9), (5,8), (4,8)')) == 'true'
    assert tolower(issquare('(4,2), (2,6), (1,3), (5,5)')) == 'true'
    assert tolower(issquare('(0,9), (7,9), (0,2), (7,2)')) == 'true'

def test_fifth():
    assert tolower(issquare('(0,2), (1,2), (1,1), (1,0)')) == 'false'
    assert tolower(issquare('(4,2), (1,1), (0,4), (3,5)')) == 'true'

def test_first():
    assert tolower(issquare('(3,2), (3,2), (5,2), (3,4)')) == 'false'
    assert tolower(issquare('(2,2), (2,2), (2,2), (2,2)')) == 'false'

def test_square():
    assert tolower(issquare('(1,7), (5,7), (1,3), (5,3)')) == 'true'
    assert tolower(issquare('(1,7), (5,7), (1,3), (9,9)')) == 'false'
    assert tolower(issquare('(1,6), (6,7), (2,7), (9,1)')) == 'false'
    assert tolower(issquare('(4,1), (3,4), (0,5), (1,2)')) == 'false'
    assert tolower(issquare('(4,6), (5,5), (5,6), (4,5)')) == 'true'

def test_square_codeeval():
    assert tolower(issquare('(5,6), (5,2), (5,6), (5,3)')) == 'false'
    assert tolower(issquare('(7,3), (2,3), (1,1), (6,1)')) == 'false'
    assert tolower(issquare('(2,2), (2,2), (2,2), (2,2)')) == 'false'
    assert tolower(issquare('(1,1), (1,9), (9,9), (9,1)')) == 'true'
    assert tolower(issquare('(8,9), (5,4), (8,6), (2,9)')) == 'false'
    assert tolower(issquare('(8,3), (9,2), (7,2), (8,1)')) == 'true'
    assert tolower(issquare('(6,0), (4,4), (3,1), (8,1)')) == 'false'
    assert tolower(issquare('(1,4), (1,0), (1,1), (2,3)')) == 'false'
    assert tolower(issquare('(2,2), (1,6), (5,7), (6,3)')) == 'true'

def test_square_codeeval2():
    assert tolower(issquare('(1,5), (1,9), (5,4), (0,3)')) == 'false'
    assert tolower(issquare('(8,3), (8,5), (9,4), (7,4)')) == 'true'
    assert tolower(issquare('(5,4), (2,3), (1,6), (4,7)')) == 'true'
    assert tolower(issquare('(5,1), (8,4), (6,1), (7,0)')) == 'false'
    assert tolower(issquare('(6,5), (2,5), (4,2), (2,8)')) == 'false'
    assert tolower(issquare('(0,2), (1,2), (1,1), (1,0)')) == 'false'

def test_square_codeeval3():
    assert tolower(issquare('(8,1), (4,7), (2,2), (6,8)')) == 'false'
    assert tolower(issquare('(2,7), (9,9), (0,0), (0,4)')) == 'false'
    assert tolower(issquare('(8,7), (7,4), (6,5), (0,8)')) == 'false'
    assert tolower(issquare('(0,2), (0,1), (1,1), (1,2)')) == 'true'


def test_permute():
    assert sorted(permute('hat')) == ['aht','ath','hat','hta','tah','tha']


def test_sorting():
    assert simplesort('70.920 -38.797 14.354 99.323 90.374 7.581') == '-38.797 7.581 14.354 70.920 90.374 99.323'
