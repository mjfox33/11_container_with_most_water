import code_11_container_with_most_water as c

def test_example_1():
    s = c.Solution()
    assert s.maxArea([1,8,6,2,5,4,8,3,7]) == 49

def test_example_2():
    s = c.Solution()
    assert s.maxArea([1,1]) == 1