'''
merge sort application prob - https://www.spoj.com/problems/INVCNT/

here while merging two sorted subarry R(right) & L(left), keeping track of if R[j] < L[i], then all L subarry elements will be inversions

so merge sort required here.
'''

def mergeTwoSortedPartandUpdate(arr, l, m, r):
    temp = []
    i = l
    j = m+1
    k = 0
    cnt = 0
    while (i<=m) and (j<=r):
        if arr[i] <= arr[j]:
            temp.append(arr[i])
            i += 1
        else:
        	cnt += (i-m+1)
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
    return cnt 


def mergeSortHelper(arr, l, r):
	c = 0
    if l < r:
        m = (l+r)//2
        c += mergeSortHelper(arr, l, m)
        c += mergeSortHelper(arr, m+1, r)
        c += mergeTwoSortedPartandUpdate(arr,l,m,r)
    return c


def sortArray(nums):
    count = mergeSortHelper(nums, 0, len(nums)-1)
    return count
    
if __name__ == "__main__":
  T = int(input().strip())
  for ti in range(T):
  	n = int(input().strip())
  	arr = []
  	for i in range(n):
  		num = int(input().strip())
  		arr.append(num)
  	print(sortArray(arr))
    
    
