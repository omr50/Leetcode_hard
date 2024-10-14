from collections import defaultdict
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        maximum = 0

        for i in range(len(points)):
            slope_map = defaultdict(lambda: 1)
            for j in range(len(points)):
                if i == j:
                    continue
                
                point1, point2 = points[i], points[j]
                x_diff = point1[0] - point2[0]
                y_diff = point1[1] - point2[1]
                
                if x_diff == 0:
                    slope_map["inf"] += 1
                    maximum = max(maximum, slope_map["inf"])
                else:
                    slope = y_diff / x_diff
                    slope_map[slope] += 1
                    maximum = max(maximum, slope_map[slope])
        if maximum == 0:
            return 1
        return maximum