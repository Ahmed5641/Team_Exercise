from problem4_code import find_gcd

def test_find_gcd_valid_inputs():
    assert find_gcd(124, 12) == (4, 2)
    assert find_gcd(476, 630) == (14, 3)
    assert find_gcd(124, 12) != (21, 4)
    
def test_find_gcd_invalid_inputs():
    try:
        find_gcd(-124, 12)
        assert False, "Expected an exception for negative input"
    except Exception:
        pass

    try:
        find_gcd(124, 0)
        assert False, "Expected an exception for input 0"
    except Exception:
        pass

    try:
        find_gcd(124.5, 12)
        assert False, "Expected an exception for float input"
    except Exception:
        pass