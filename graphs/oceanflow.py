class Solution:
    def pacificAtlantic(self, heights):
        answers = []
        visited = set()
        for r in range(len(heights)):
            for c in range(len(heights[0])):
                pacific = False
                atlantic = False
                self.reach(heights,r,c,pacific,atlantic,visited)
                if pacific and atlantic:
                    answers.append([r,c])

        return answers

    def reach(self,heights,r,c,pacific,atlantic,visited):
        if r == 0 or c == 0:
            pacific = True
        if r == len(heights) or c == len(heights[0]):
            atlantic = True
        pos = str(r)+','+str(c)

        if pos in visited:
            pacific = True
            atlantic = True
            return
        if pacific and atlantic:
            visited.add(pos)
            return

        print(pacific)
        print(atlantic)
        if not pacific:
            if heights[r-1][c] <= heights[r][c]:
                self.reach(heights,r-1,c,pacific,atlantic,visited)
            if heights[r][c-1] <= heights[r][c]:
                self.reach(heights,r,c-1,pacific,atlantic,visited)

        if not atlantic:
            print(r)
            print(c)
            if heights[r+1][c] <= heights[r][c]:
                self.reach(heights,r+1,c,pacific,atlantic,visited)

            if heights[r][c+1] <= heights[r][c]:
                self.reach(heights,r,c+1,pacific,atlantic,visited)
heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
ocean = Solution()
print(ocean.reach(heights,1,4,False,False,set()))