class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2
        if len(A) > len(B):
            A, B = B, A 
            
        l, r = 0, len(A) - 1
        even = ((total) & 1) == 0
        while True:
            m = (l + r) // 2
            m2 = half - m - 2

            # find out if they are consecutive
            nums1_Lower = A[m] if m >= 0 else float('-inf')
            nums1_Upper = A[m + 1] if m+1 < len(A) else float('inf')
            nums2_Lower = B[m2] if m2 >= 0 else float('-inf')
            nums2_Upper = B[m2 + 1] if m2+1 < len(B) else float('inf')
            # consecutive
            if nums1_Lower <= nums2_Upper and nums2_Lower <= nums1_Upper:
                if even:
                    print(m, m2)
                    # return the highest of the lower bound, and the lowest of the upper bound divided by 2
                    return (max(nums1_Lower, nums2_Lower) + min(nums1_Upper, nums2_Upper)) / 2
                else:
                    return min(nums1_Upper, nums2_Upper)
            elif nums1_Lower > nums2_Upper:
                r = m - 1
            else:
                l = m + 1


        # A, B = nums1, nums2
        # total = len(nums1) + len(nums2)
        # half = total // 2

        # if len(B) < len(A):
        #     A, B = B, A

        # l, r = 0, len(A) - 1
        # while True:
        #     i = (l + r) // 2
        #     j = half - i - 2

        #     Aleft = A[i] if i >= 0 else float("-infinity")
        #     Aright = A[i + 1] if (i + 1) < len(A) else float("infinity")
        #     Bleft = B[j] if j >= 0 else float("-infinity")
        #     Bright = B[j + 1] if (j + 1) < len(B) else float("infinity")

        #     if Aleft <= Bright and Bleft <= Aright:
        #         if total % 2:
        #             return min(Aright, Bright)
        #         return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
        #     elif Aleft > Bright:
        #         r = i - 1
        #     else:
        #         l = i + 1