'''
1. Find the duplicate number in an array
(allow to modify the array)

2. For a 2D dimension array where rows increase from left to  right
and columns increase from top to bottom.
Define a function which is able to decide whether the array contains a specific number.
'''

class Solution1:
    def finddup (self,nums):
        com=set(nums)
        dup = list(set(nums) - com)
        return dup

    def finddup2 (self,nums):
        l2 = []
        for i in nums:
            if i not in nums:
                l2.append(i)
        dup = list(set(nums) - set(l2))
        return dup

# start to search from the top right of the matrix.
# If the element is larger than target, exclude the right column.
# If the element is smaller than target, exclude the top row
class Solution2:
    def Find (self,array, target):
        if array == []:
            return (False)
        rows = len(array)
        cols = len(array[0])

        row = 0
        col = cols - 1
        while col>=0 and row<rows:
            if array[row][col]>target:
                col -= 1
            elif array[row][col]<target:
                row += 1
            else:
                return (row, col)
        return(False)

array1 = [[1, 2, 8, 9],
         [2, 4, 9, 12],
         [4, 7, 10, 13],
         [6, 8, 11, 15]]

array2 = [2,3,5,6,6,3,2,3,5234,52]
find = Solution1()
print(find.finddup2(array2))

findtarget = Solution2()
print(findtarget.Find(array1,100))