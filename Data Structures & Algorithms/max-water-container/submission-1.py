class Solution:
    def maxArea(self, heights: List[int]) -> int:

    
        '''   
            two pointer problem because we are always comparing two heights as we iterate through. Start at end and find the area, and only update answer if area is greater. After this, move the smaller of the pointers. If the pointers are equal move both
        '''

        left = 0
        right = len(heights) - 1
        ans = 0

        while left < right:

            height = min(heights[left], heights[right])
            width = right - left

            ans = max(ans, height * width)

            if heights[left] > heights[right]:
                right -= 1

            elif heights[left] < heights[right]:
                left += 1

            else:
                left += 1
                right -= 1
        
        return ans


        