
from fighting import deathCheck

def test_deathCheck():
    '''test deathCheck(health, char)'''
    assert(deathCheck(10, False) == False)
    assert(deathCheck(5, False) == False)
    assert(deathCheck(1, False) == False)
    assert(deathCheck(0, False) == True)
    assert(deathCheck(-5, False) == True)
