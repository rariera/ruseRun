
from fighting import deathCheck

def test_deathCheck():
    '''test deathCheck(being, health, char)'''
    assert(deathCheck(None, 10, False) == False)
    assert(deathCheck(None, 5, False) == False)
    assert(deathCheck(None, 1, False) == False)
    assert(deathCheck(None, 0, False) == True)
    assert(deathCheck(None, -1, False) == True)
    assert(deathCheck(None, -5, False) == True)
