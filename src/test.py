"""
Module for testing the merge_sort function from hw2_debugging.
Contains test cases to validate the sorting functionality.
"""

from hw2_debugging import merge_sort

def test_case1():
    """
    Test merge_sort with a list of distinct integers.
    """
    arr = [34, 7, 23, 32, 5, 62]
    expected = [5, 7, 23, 32, 34, 62]
    assert merge_sort(arr) == expected
    print("Test Case 1 Passed!")


def test_case2():
    """
    Test merge_sort with a list containing duplicates.
    """
    arr = [10, 22, 10, 14, 22, 7]
    expected = [7, 10, 10, 14, 22, 22]
    assert merge_sort(arr) == expected
    print("Test Case 2 Passed!")


def test_case3():
    """
    Test merge_sort with an empty list.
    """
    arr = []
    expected = []
    assert merge_sort(arr) == expected
    print("Test Case 3 Passed!")


if __name__ == "__main__":
    test_case1()
    test_case2()
    test_case3()
