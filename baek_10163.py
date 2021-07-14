import sys
N = int(sys.stdin.readline())
square_info = []
arr = []
for n in range(N):
    square_info.append(list(map(int, sys.stdin.readline().split())))
print(square_info, arr)

# end point
for square in square_info:
    square[2] = square[0]+square[2] - 1
    square[3] = square[1]+square[3] - 1

# i 넣기
for i, square in enumerate(square_info):
    x1, y1 = square[0], square[1]
    x2, y2 = square[2], square[3]