class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        h=max(candies)
        print(h)
        k=[]
        for i in candies:
            k.append(i+extraCandies >=h)
        return k