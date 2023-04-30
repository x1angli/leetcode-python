# Python code to demonstrate the working of
# bisect(), bisect_left() and bisect_right()

# importing "bisect" for bisection operations
import bisect


def bisect_left_impl(arr, tgt_val, l_idx: int = 0, r_idx: int = None):
    if l_idx < 0:
        raise ValueError('l must be non-negative')
    if r_idx is None:
        r_idx = len(arr)

    while l_idx < r_idx:
        mid = (l_idx + r_idx) // 2
        if arr[mid] >= arr[tgt_val]:
            r_idx = mid
        else:
            l_idx = mid + 1
    return l_idx


def bisect_right_impl(arr, tgt_val, l_idx: int = 0, r_idx: int = None):
    if l_idx < 0:
        raise ValueError('l must be non-negative')
    if r_idx is None:
        r_idx = len(arr)

    while l_idx < r_idx:
        mid = (l_idx + r_idx) // 2
        if arr[mid] > arr[tgt_val]:
            r_idx = mid
        else:
            l_idx = mid + 1
    return l_idx



li = [1, 3, 4, 4, 4, 6, 7]

# using bisect() to find right most possible index
ans = bisect.bisect(li, 4)
print(f"bisect.bisect[_right](li, 4) : {ans} ")

# using bisect_left() to find left most possible index
ans = bisect.bisect_left(li, 4)
print(f"bisect.bisect_left(li, 4)  {ans} ")

# using bisect_left() to find left most possible index
ans = bisect_left_impl(li, 4)
print(f"bisect_left_selfimpl(li, 4)  {ans} ")

ans = bisect_right_impl(li, 4)
print(f"bisect_right_impl(li, 4)  {ans} ")
