def max_sum_subarray(arr, k):
    n = len(arr)
    
    # Edge Case: If the array is smaller than the window, we can't do it.
    if n < k:
        return -1
    
    # STEP 1: Calculate the sum of the FIRST window manually
    # We slice from index 0 to k
    window_sum = sum(arr[:k]) 
    max_sum = window_sum
    
    # STEP 2: Slide the window across the rest of the array
    # Start loop from the 'k'th element because we already did the first k
    for i in range(k, n):
        
        # KEY LOGIC:
        # 1. Add the new element (arr[i])
        # 2. Subtract the element that goes out of the window (arr[i - k])
        
        window_sum = window_sum + arr[i] - arr[i - k]
        
        # Check if this new sum is the biggest we've seen
        max_sum = max(max_sum, window_sum)
        
    return max_sum

# --- Testing ---
nums = [2, 1, 5, 1, 3, 2]
k = 3
print(f"Maximum Sum: {max_sum_subarray(nums, k)}")
# Output: 9 (which is 5 + 1 + 3)