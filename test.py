from main_function import main_fun

def test_get_value():
    # Test 1: Test retrieval from example given
    data1 = {"a": {"b": {"c": "d"}}}
    result1 = main_fun(data1, "a/b/c")
    assert result1 == "d", f"Test 1 failed: expected 'd', got {result1}"

    # Test 2: Test with different words from the PDF given
    data2 = {"x": {"y": {"z": "a"}}}
    result2 = main_fun(data2, "x/y/z")
    assert result2 == "a", f"Test 2 failed: expected 'a', got {result2}"

    # Test 3: Test for a non-existent key
    data3 = {"p": {"q": {"r": "s"}}}
    result3 = main_fun(data3, "p/q/x")
    assert result3 is None, f"Test 3 failed: expected None, got {result3}"

    # Test 4: Test for longer dic
    data4 = {"p": {"q": {"r": {"x":"s"}}}}
    result4 = main_fun(data4, "p/q/r/x")
    assert result4 is None, f"Test 4 failed: expected None, got {result4}"

    # Test 5: Test with an empty dictionary
    data5 = {}
    result5 = main_fun(data4, "a/b/c")
    assert result5 is None, f"Test 5 failed: expected None, got {result5}"

    # Test 6: Test with a non-string value
    data6 = {"num": {"val": {"x": 42}}}
    result6 = main_fun(data5, "num/val/x")
    assert result6 == 42, f"Test 6 failed: expected 42, got {result6}"

    print("All tests passed!")

if __name__ == "__main__":
    test_get_value()
