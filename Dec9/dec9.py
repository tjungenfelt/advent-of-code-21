import fileinput

lines = []
with fileinput.input(files=('input.txt')) as f:
    for line in f:
        lines.append(line.strip())

height = []
for i in lines:
    height.append([int(x) for x in i ])

marked = [[False]*len(height[0]) for elem in height[0]]
final = 0

for i in range(0,len(height)):
    for j in range(len(height[0])):
        if i == 0:
            if j == 0:
                n = [height[i][j + 1], height[i + 1][j]]
            elif j == len(height[0])-1:
                n = [height[i][j - 1], height[i + 1][j]]
            else:
                n = [height[i][j + 1], height[i][j - 1], height[i + 1][j]]
        elif j == 0:
            if i == len(height)-1:
                n = [height[i][j + 1], height[i - 1][j]]
            else:
                n = [height[i][j + 1], height[i - 1][j], height[i + 1][j]]
        elif i == len(height)-1:
            if j == len(height[0])-1:
                n = [height[i][j - 1], height[i - 1][j]]
            else:
                n = [height[i][j + 1], height[i][j - 1], height[i - 1][j]]
        elif j == len(height[0])-1:
            n = [height[i + 1][j], height[i][j - 1], height[i - 1][j]]
        else:
            n = [height[i + 1][j], height[i][j - 1], height[i - 1][j], height[i][j + 1]]
        bool = []
        for num in n:
            if height[i][j] < num:
                bool.append(True)
            else:
                bool.append(False)
        if (sum(bool) == len(bool)):
            final += height[i][j] + 1

print(final)






