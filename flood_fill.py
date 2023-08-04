class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        stack = collections.deque()
        changed_pixels = set()
        stack.append((sr, sc))
        original_color = image[sr][sc]
        while len(stack)>0:
            i, j = stack.pop()
            image[i][j] = color
            changed_pixels.add(str(i)+str(j))
            for di in [-1, 0, 1]:
                for dj in [0, -1, 1]:
                    # if we are not going diagonally
                    if (di == 0 or dj == 0) \
                    and 0 <= i + di < len(image) \
                    and 0 <= j + dj < len(image[0]) \
                    and image[i + di][j + dj] == original_color \
                    and str(i + di) + str(j + dj) not in changed_pixels:
                        stack.append((i + di, j + dj))
        return image
