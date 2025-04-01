from main_function import main_fun

def test_get_value():
    # Test 1: Test retrieval from example given
    data1 = {"a": {"b": {"c": "d"}}}
    result1 = main_fun(data1, "a/b/c")
    assert result1 == "d", f"Test 1 failed: expected 'd', got {result1}"
    print("Test 1 passed")

    # Test 2: Test with different words from the PDF given
    data2 = {"x": {"y": {"z": "a"}}}
    result2 = main_fun(data2, "x/y/z")
    assert result2 == "a", f"Test 2 failed: expected 'a', got {result2}"
    print("Test 2 passed")

    # Test 3: Test for a non-existent key
    data3 = {"p": {"q": {"r": "s"}}}
    result3 = main_fun(data3, "p/q/x")
    assert result3 is None, f"Test 3 failed: expected None, got {result3}"
    print("Test 3 passed")

    # Test 4: Test for longer dic
    data4 = {"p": {"q": {"r": {"x":"s"}}}}
    result4 = main_fun(data4, "p/q/r/x")
    assert result4 == "s", f"Test 4 failed: expected None, got {result4}"
    print("Test 4 passed")

    # Test 5: Test with an empty dictionary
    data5 = {}
    result5 = main_fun(data5, "a/b/c")
    assert result5 is None, f"Test 5 failed: expected None, got {result5}"
    print("Test 5 passed")

    # Test 6: Test with a non-string value
    data6 = {"num": {"val": {"x": 42}}}
    result6 = main_fun(data6, "num/val/x")
    assert result6 == 42, f"Test 6 failed: expected 42, got {result6}"
    print("Test 6 passed")

    print("All tests passed!")

if __name__ == "__main__":
    test_get_value()
