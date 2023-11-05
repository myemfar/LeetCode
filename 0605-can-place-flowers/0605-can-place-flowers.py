class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        toAdd = n
        for i in range(len(flowerbed)):
            if i == 0:
                if len(flowerbed) == 1 and flowerbed[i] == 0:
                    toAdd -= 1
                elif flowerbed[i] == 0 and flowerbed[1] == 0:
                    flowerbed[i] = 1
                    toAdd -= 1
            elif i == len(flowerbed)-1:
                if flowerbed[i-1] == 0 and flowerbed[i] == 0:
                    toAdd -= 1
            else:
                if flowerbed[i-1] == 0 and flowerbed[i] == 0 and flowerbed[i+1] == 0:
                    flowerbed[i] = 1
                    toAdd -= 1
        if toAdd < 1:
            return True
        else:
            return False



