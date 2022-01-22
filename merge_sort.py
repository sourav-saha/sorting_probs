'''
merge sort: divide & concur alog
TC: NlogN
SC: N
depth of recursion: LogN

https://leetcode.com/problems/sort-an-array/submissions/
'''

def mergeTwoSortedPartandUpdate(arr, l, m, r):
    temp = []
    i = l
    j = m+1

    while (i<=m) and (j<=r):
        if arr[i] <= arr[j]:
            temp.append(arr[i])
            i += 1
        else:
            temp.append(arr[j])
            j += 1
    
    #rest, if any
    while i <= m:
        temp.append(arr[i])
        i += 1
    while j<=r:
        temp.append(arr[j])
        j += 1
    
    #copy to arr
    arr[l:r+1] = temp
    #for i in range(l, r+1):
    #    arr[i] = temp[i-l]


def mergeSortHelper(arr, l, r):
    if l < r:
        m = (l+r)//2
        mergeSortHelper(arr, l, m)
        mergeSortHelper(arr, m+1, r)
        mergeTwoSortedPartandUpdate(arr,l,m,r)

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        mergeSortHelper(nums, 0, len(nums)-1)
        return nums
      
      
