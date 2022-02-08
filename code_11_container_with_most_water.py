class Solution:
    def maxArea(self, height: list[int]) -> int:
        n = len(height)
        if n == 2:
            return min(height)

        max_area = 0
        current_area = 0
        left_pointer = 0
        right_pointer = n-1

        while left_pointer < right_pointer:
            if height[left_pointer] < height[right_pointer]:
                current_area = height[left_pointer] * (right_pointer - left_pointer)
                left_pointer += 1
            else:
                current_area = height[right_pointer] * (right_pointer - left_pointer)
                right_pointer -= 1
            max_area = max(max_area, current_area)
        return max_area
        