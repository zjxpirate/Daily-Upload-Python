

# 2. search a maze

import collections

WHITE, BLACK = range(2)

maz = [[0, 0, 1, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 1, 0], [1, 0, 0, 1], [0, 0, 0, 1]]

Coordinate = collections.namedtuple('Coordinate', ('x', 'y'))

start = Coordinate(x=2, y=1)
end = Coordinate(x=2, y=0)

def search_maze(maze, s, e):
    # Perform DFS to find a feasible path.
    def search_maze_helper(cur):
        # checks cur is within maze and is a white pixel.
        if not (0 <= cur.x < len(maze) and 0 <= cur.y < len(maze[cur.x]) and maze[cur.x][cur.y] == WHITE):
            return False

        path.append(cur)
        maze[cur.x][cur.y] = BLACK

        if cur == e:
            return True

        if any(map(search_maze_helper, map(Coordinate, (cur.x - 1, cur.x + 1, cur.x, cur.x), (cur.y, cur.y, cur.y - 1, cur.y + 1)))):
            return True

        # cannot find a path, remove the entry added in path.append(cur).
        del path[-1]
        return False

    path = []
    search_maze_helper(s)
    return path


print(search_maze(maz, start, end))

