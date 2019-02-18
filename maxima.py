def find_maxima(x):
    """Find local maxima of x.

    Example:
    >>> x = [1, 2, 3, 2, 4, 3]
    >>> find_maxima(x)
    [2, 4]

    Input arguments:
        x -- 1D list numbers

    Output:
        idx -- list of indices of the local maxima in x
    """

    idx = []
    for i in range(len(x)):
        # `i` is a local maximum if the signal decreases before and...
        if x[i-1] < x[i]:
            # ...it's the last element
            if i == len(x)-1:
                idx.append(i)
            # ...after it
            elif x[i+1] < x[i]:
                idx.append(i)
            # ...the directly following elements are same or smaller
            elif following_elements_are_same_or_smaller(x, i):
                idx.append(i)
    return idx

def following_elements_are_same_or_smaller(x, i):
    for j in range(i+1, len(x)):
        if x[i] < x[j]:
            return False
    return True
