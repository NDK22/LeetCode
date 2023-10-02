
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

        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
