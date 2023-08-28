"""
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n,
representing the number of elements in nums1 and nums2 respectively.
Merge nums1 and nums2 into a single array sorted in non-decreasing order.
"""

def merge(nums1, m, nums2, n):
    i = m - 1
    j = n - 1
    merged_index = m + n - 1
    
    while i >= 0 and j >= 0:
        if nums1[i] > nums2[j]:
            nums1[merged_index] = nums1[i]
            i -= 1
        else:
            nums1[merged_index] = nums2[j]
            j -= 1
        
        merged_index -= 1
        
    
    while j >= 0:
        nums2[merged_index] = nums2[j]
        j -= 1

if __name__ == "__main__":
    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [2,5,6]
    n = 3
    merge(nums1, m, nums2, n)
    print(nums1)