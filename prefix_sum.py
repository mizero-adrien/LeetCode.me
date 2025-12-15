#prefix sum allow to create sum of subarray in time O(1)
#this is to find sum of array from one indes to another index

def build_prefix(arr):
    prefix = [0] * len(arr)
    prefix[0] = arr[0]

    for i in range(1, len(arr)):
        prefix[i] = prefix[i - 1] + arr[i]

    return prefix

def range_sum(prefix, L, R):
    if L == 0:
        return prefix[R]
    return prefix[R] - prefix[L - 1]

arr = [2, 4, 3, 5]
prefix = build_prefix(arr)

print(range_sum(prefix, 1, 3))  # Output: 12
