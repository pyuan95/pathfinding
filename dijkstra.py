class Node:
    def __init__(self, x, y, parent = None, G = 0):
        self.x = x
        self.y = y
        self.parent = parent
        self.G = G

    def get_neighbor_locs(self):
        locs = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                if sum([abs(i), abs(j)]) == 1:
                    locs.append([i + self.x, j + self.y])
        return locs

    def equals(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        return False

    def print(self):
        print("row: ", self.x, "col: ", self.y)


def min_gcost(l):
    n = l[0]
    for node in l:
        if node.G < n.G:
            n = node
    return n


def get_node_from_list(n, l):
    for node in l:
        if n.equals(node):
            return node
    return None


def in_list(n, l):
    return get_node_from_list(n, l) is not None


def remove_node_from_list(n, l):
    for i, node in enumerate(l):
        if n.equals(node):
            l.pop(i)
            return


def is_valid(n, m):
    c = m[n.x][n.y]
    return not (c == " " or c == "#")


def get_map():
    m = list()
    while True:
        i = input()
        if i != "":
            m.append([x for x in i])
        else:
            break
    return m


def get_start_loc(m):
    for i, row in enumerate(m):
        for j, col in enumerate(row):
            if col == "$":
                return i, j


def get_end_loc(m):
    for i, row in enumerate(m):
        for j, col in enumerate(row):
            if col == "&":
                return i, j


def print_path(end, map):
    end = end.parent
    while end.parent is not None:
        x, y = end.x, end.y
        end = end.parent
        map[x][y] = "x"
    [print("".join(row)) for row in map]


def find_path(m, par, end, open_list, closed_list):
    if par.equals(end):
        print("Length of shortest path: ", par.G)
        return par

    remove_node_from_list(par, open_list)
    closed_list.append(par)

    for loc in par.get_neighbor_locs():
        n = Node(loc[0], loc[1], par, par.G + 1)
        if not in_list(n, closed_list) and is_valid(n, m):
            if in_list(n, open_list):
                prev = get_node_from_list(n, open_list)
                if n.G < prev.G:
                    remove_node_from_list(prev, open_list)
                    open_list.append(n)
            else:
                open_list.append(n)

    if len(open_list) == 0:
        print("No Path!")
        return None

    par = min_gcost(open_list)
    return find_path(m, par, end, open_list, closed_list)


def main():
    m = get_map()
    start = get_start_loc(m)
    end = get_end_loc(m)
    start_node = Node(start[0], start[1])
    end_node = Node(end[0], end[1])
    end_node = find_path(m, start_node, end_node, [start_node], [])
    if end_node:
        print("\nPath:\n")
        print_path(end_node, m)


if __name__ == "__main__":
    main()





