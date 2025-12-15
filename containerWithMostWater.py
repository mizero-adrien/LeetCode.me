class Solution:
    def maxArea(self, height):
        i, j = 0, len(height) - 1
        max_area = 0

        while i < j:
            h = min(height[i], height[j])
            area = h * (j - i)
            max_area = max(max_area, area)

            # Move the pointer at the shorter line
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1

        return max_area
