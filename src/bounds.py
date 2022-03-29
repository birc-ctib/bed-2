"""
Module for experimenting with lower and upper bounds.

Unlike in the BED functionality, where we need to search for a lower bound in
a list of features, here we only concern ourselves with lists of integers.
"""


def lower_bound(x: list[int], v: int) -> int:
    """Get the index of the lower bound of v in x.

    If all values in x are smaller than v, return len(x).
    """
    lo, hi = 0, len(x)
    while lo < hi:
        m = (lo + hi) // 2
        if x[m] < v:
            lo = m + 1
        else:
            hi = m
    return lo


def upper_bound(x: list[int], v: int) -> int:
    """Get the index of the upper bound of v in x.

    If all values in x are smaller than v, return len(x).
    """
    # Since we are working with integers, this trick will work.
    # You can't always have a "next" value like here, and then there
    # is a little more work to it, but this is the simplest
    # way to get an upper bound when there is a next.
    return lower_bound(x, v+1)
