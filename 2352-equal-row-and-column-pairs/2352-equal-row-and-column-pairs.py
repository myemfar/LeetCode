class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        vertical_arrays = []
        for i in range(len(grid)):
            column_vals = []
            for row in grid:
                column_vals.append(row[i])
            vertical_arrays.append(column_vals)
        matches = 0
        for column in vertical_arrays:
            for row in grid:
                if column == row:
                    matches += 1
        return matches