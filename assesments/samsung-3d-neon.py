import numpy as np

#input = [[1, 240, 1, 235, 240, 1, 235, 1, 230], 3, [0, 1]]
#output = [0, 1, 0, 1, 1, 0, 1, 0, 0]

#input = [[1, 240, 1, 235, 240, 1, 235, 1, 230], 3, [0, 2]]
#output = [0, 0, 0, 0, 0, 0, 0, 0, 0]

input = [[1, 240, 1, 1, 240, 1, 1, 240, 1, 1, 240, 1, 1, 1, 255, 255, 255, 1, 1, 1, 1, 1, 225, 220, 1, 1, 1, 1,
          230, 210, 230, 230, 230, 230, 230, 210], 6, [2, 2]]

def to_matrix(lst, n):
    return [lst[i:i+n] for i in range(0, len(lst), n)]

image = input[0]
image = to_matrix(image, input[1])
n = input[1]
mask = [[0 for j in range(0,n)] for i in range(0, n)]
img_cp = [[image[i][j] for j in range(0,n)] for i in range(0, n)]

roi_y = input[2][0]
roi_x = input[2][1]

def coherent_region(y, x):
    if y < 0 or x < 0 or y >=len(image) or x>= len(image[0]) or img_cp[y][x] < 200:
        return
    mask[y][x] = 1
    img_cp[y][x] = 0
    coherent_region(y+1, x)
    coherent_region(y-1, x)
    coherent_region(y, x+1)
    coherent_region(y, x-1)

coherent_region(roi_y, roi_x)

print(mask)



