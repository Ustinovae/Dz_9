from PIL import Image
import numpy as np
img = Image.open("dog.jpg")
arr = np.array(img)
a = len(arr)
a1 = len(arr[1])
i = 0
while i < a - 11:
    j = 0
    while j < a1 - 11:
        s = 0
        for x in range(i, i + 10):
            for y in range(j, j + 10):
                n1 = arr[x][y][0]
                n2 = arr[x][y][1]
                n3 = arr[x][y][2]
                M = n1/3 + n2/3 + n3/3
                s += M
        s = int(s // 100)
        for n in range(i, i + 10):
            for n1 in range(j, j + 10):
                arr[n][n1][0] = int(s // 50) * 50
                arr[n][n1][1] = int(s // 50) * 50
                arr[n][n1][2] = int(s // 50) * 50
        j = j + 10
    i = i + 10
res = Image.fromarray(arr)
res.save('old_filter_res.jpg')