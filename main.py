"""
CMPS 2200  Assignment 1.
See assignment-01.pdf for details.
"""
# no imports needed.

def foo(x):
    if x <= 1:
        return x
    ra = foo(x - 1)
    rb = foo(x - 2)
    return ra + rb

def longest_run(mylist, key):
    best = 0
    cur = 0
    for v in mylist:
        if v == key:
            cur += 1
            if cur > best:
                best = cur
        else:
            cur = 0
    return best


class Result:
    """ done """
    def __init__(self, left_size, right_size, longest_size, is_entire_range):
        self.left_size = left_size               # run on left side of input
        self.right_size = right_size             # run on right side of input
        self.longest_size = longest_size         # longest run in input
        self.is_entire_range = is_entire_range   # True if the entire input matches the key
        
    def __repr__(self):
        return('longest_size=%d left_size=%d right_size=%d is_entire_range=%s' %
              (self.longest_size, self.left_size, self.right_size, self.is_entire_range))
    

def to_value(v):
    """
    if it is a Result object, return longest_size.
    else return v
    """
    if type(v) == Result:
        return v.longest_size
    else:
        return int(v)
        
def longest_run_recursive(mylist, key):
    n = len(mylist)
    if n == 0:
        return Result(0, 0, 0, True)
    if n == 1:
        if mylist[0] == key:
            return Result(1, 1, 1, True)
        else:
            return Result(0, 0, 0, False)

    mid = n // 2
    left_res  = longest_run_recursive(mylist[:mid], key)
    right_res = longest_run_recursive(mylist[mid:], key)

    # entire range is all key only if both halves are all key
    is_entire = left_res.is_entire_range and right_res.is_entire_range

    # prefix run can extend from left half into right half if left half is all key
    left_size = left_res.left_size + right_res.left_size if left_res.is_entire_range else left_res.left_size

    # suffix run can extend from right half into left half if right half is all key
    right_size = right_res.right_size + left_res.right_size if right_res.is_entire_range else right_res.right_size

    # best run is in left, in right, or crossing the middle
    cross = left_res.right_size + right_res.left_size
    longest_size = max(left_res.longest_size, right_res.longest_size, cross)

    return Result(left_size, right_size, longest_size, is_entire)



