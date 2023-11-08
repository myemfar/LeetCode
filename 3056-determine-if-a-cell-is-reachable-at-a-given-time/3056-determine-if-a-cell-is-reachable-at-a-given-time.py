class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        x_dist = abs(sx-fx)
        y_dist = abs(sy-fy)
        if (sy == fy and sx == fx and t == 1):
            return False
        return (x_dist <= t and y_dist <= t)
