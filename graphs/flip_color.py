

# 3. paint a boolean matrix

paint = [[0, 0, 1, 0, 1, 0],
         [0, 1, 0, 1, 0, 0],
         [1, 0, 1, 0, 0, 0],
         [0, 1, 0, 0, 0, 0]]

import collections

def flip_color(x, y, image):
    color = image[x][y]
    q = collections.deque([(x, y)])
    image[x][y] = 1 - image[x][y]   # flips.
    while q:
        x, y = q.popleft()
        for next_x, next_y in ((x, y + 1), (x, y - 1), (x + 1, y), (x - 1, y)):
            if (0 <= next_x < len(image) and 0 <= next_y < len(image[next_x]) and image[next_x][next_y] == color):
                # flips the color.
                image[next_x][next_y] = 1 - image[next_x][next_y]
                q.append((next_x, next_y))


flip_color(3, 5, paint)
print(paint)



def flip_color_recursion(x, y, image):
    color = image[x][y]
    image[x][y] = 1 - image[x][y] # flips
    for next_x, next_y in ((x, y + 1), (x, y - 1), (x + 1, y), (x - 1, y)):
        if (0 <= next_x < len(image) and 0 <= next_y < len(image[next_x]) and image[next_x][next_y] == color):
            flip_color_recursion(next_x, next_y, image)

flip_color_recursion(3, 5, paint)
print(paint)

