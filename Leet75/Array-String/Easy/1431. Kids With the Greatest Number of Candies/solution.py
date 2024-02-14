#solution 1
class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        maximum = max(candies)
        list = []
        for i in range(len(candies)):
            candies[i] = candies[i] + extraCandies
            if candies[i] >= maximum:
                list.append(True)
            else:
                list.append(False)
        return list

#solution 2
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        highest_num = max(candies)
        result =[]
        for candy in candies:
            result.append(candy + extraCandies >= highest_num)
        return result
