class Solution:
    __privateNumber = 0

    def sum(self):
        self.__privateNumber += 1
        print(self.__privateNumber)


count = Solution()
print(count._Solution__privateNumber)
print(dir(count))
count.sum()
count.sum()