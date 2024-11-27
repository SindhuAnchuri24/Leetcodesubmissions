class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        m = len(flowerbed)
        flag=0
        for i in range(m):
            if i!=0 and i!=m-1 and flowerbed[i]==0:
                if flowerbed[i-1]==0 and flowerbed[i+1]==0:
                    flowerbed[i]=1
                    n-=1
            elif i==0 and flowerbed[i]==0 and i!=m-1:
                if flowerbed[i+1]==0:
                    flowerbed[i]=1
                    n-=1
            elif i==m-1  and flowerbed[i]==0:
                if flowerbed[i-1]==0:
                    flowerbed[i]=1
                    n-=1
        if n>0:
            return False
        else:
            return True