import random

class Node:
    def __init__(self, a, b, z, parent=None):
        self.x = a
        self.y = b
        self.depth = z
        self.parent = parent

class DFS:
    def __init__(self):
        self.directions = 4
        self.x_move = [1, -1, 0, 0]
        self.y_move = [0, 0, 1, -1]
        self.found = False
        self.N = random.randint(4, 7)
        self.grid = self.generate_grid(self.N)
        self.path = []
        self.topo_order = []
        self.set_source_and_goal()
        self.start_dfs()

    def generate_grid(self, N):
        return [[random.choice([0, 1]) for _ in range(N)] for _ in range(N)]

    def set_source_and_goal(self):
        while True:
            sx = random.randint(0, self.N - 1)
            sy = random.randint(0, self.N - 1)
            gx = random.randint(0, self.N - 1)
            gy = random.randint(0, self.N - 1)
            if (sx != gx or sy != gy) and self.grid[sx][sy] == 1 and self.grid[gx][gy] == 1:
                break
        self.source = Node(sx, sy, 0)
        self.goal = Node(gx, gy, 999999)
        self.source_pos = (sx, sy)
        self.goal_pos = (gx, gy)

    def print_grid(self):
        for i in range(self.N):
            row = ""
            for j in range(self.N):
                if (i, j) == self.source_pos:
                    row += "S "
                elif (i, j) == self.goal_pos:
                    row += "G "
                elif self.grid[i][j] == 1:
                    row += ". "
                else:
                    row += "# "
            print(row)
        print()

    def start_dfs(self):
        print(f"Generated {self.N}x{self.N} grid:\n")
        self.print_grid()
        print("Source:", self.source_pos)
        print("Goal:", self.goal_pos)
        self.dfs(self.source)
        if self.found:
            print("\n Path")
            self.build_path()
            for p in self.path:
                print(p, end=" -> ")
            print("Goal")
        else:
            print("\nNot foun")

        print("\nOrdeR")
        for pos in self.topo_order:
            print(pos, end=" -> ")
        print("End")

    def dfs(self, u):
        self.grid[u.x][u.y] = 0
        self.topo_order.append((u.x, u.y))
        if (u.x, u.y) == (self.goal.x, self.goal.y):
            self.found = True
            self.goal.depth = u.depth
            self.goal.parent = u.parent
            return
        for j in range(self.directions):
            v_x = u.x + self.x_move[j]
            v_y = u.y + self.y_move[j]
            if 0 <= v_x < self.N and 0 <= v_y < self.N and self.grid[v_x][v_y] == 1:
                child = Node(v_x, v_y, u.depth + 1, parent=u)
                self.dfs(child)
                if self.found:
                    return

    def build_path(self):
        node = self.goal
        while node:
            self.path.insert(0, (node.x, node.y))
            node = node.parent

def main():
    DFS()

if __name__ == "__main__":
    main()
