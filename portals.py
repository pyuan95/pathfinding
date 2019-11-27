def minGCost(l):
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

def remove_node_from_list(n, l):
    for i, node in enumerate(l):
        if n.equals(node):
            l.pop(i)
            return

def is_valid(n, portals):
    c = portals[n.x][n.y]
    return not (c == " " or c == "#")


def is_portal(x, y, portals):
    # print(x," ", y)
    c = portals[x][y]
    return c.isalpha()

def get_other_portal(x, y, portals):
    c = portals[x][y]
    for i, row in enumerate(portals):
        for j, ch in enumerate(row):
            if c == ch and not (x == i and y == j):
                return i, j

def print_path(end, map):
    end = end.parent
    while end.parent is not None:
        x, y = end.x, end.y
        end = end.parent
        map[x][y] = "x"
    [print("".join(row)) for row in map]


class Node:

    def __init__(self, x, y, parent = None, G = 0):
        self.x = x
        self.y = y
        self.parent = parent
        self.isClosed = False
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

# print(portals, "rows: ", len(portals), "cols: ", len(portals[0]))

def find_path(portals):
    start = None
    end = None
    for i, row in enumerate(portals):
        for j, n in enumerate(row):
            if n == "$":
                start = Node(i, j, None)
            if n == "&":
                end = Node(i, j, None)

    par = Node(start.x, start.y, None) # set the start node as parent

    open = [par] # add start node to the open list
    closed = [] # init closed list
#hi this is sara fish are great, have a nice day!
    while len(open) != 0: # while the open list is not empty
        remove_node_from_list(par, open) # remove from open list
        closed.append(par) # add to the closed list
        for loc in par.get_neighbor_locs(): # for every neighbor to parent
            n = None
            if is_portal(loc[0], loc[1], portals):
                x, y = get_other_portal(loc[0], loc[1], portals)
                n = Node(x, y, par, par.G + 1)
                n1 = Node(loc[0], loc[1], par, par.G + 1)
                closed.append(n1)
            else:
                n = Node(loc[0], loc[1], par, par.G + 1)
            if get_node_from_list(n, closed) is None and is_valid(n, portals): # if neighbor is not closed or invalid (border, wall)
                if get_node_from_list(n, open) is not None: # if neighbor is in the open list
                    prev = get_node_from_list(n, open)
                    if n.G < prev.G: # update G if current G is smaller than prev G
                        open.append(n)
                        remove_node_from_list(prev, l)
                else: # if it isn't in the open list, add it
                    open.append(n)
            else: # if it is closed or invalid, skip
                continue

        n = minGCost(open)
        par = n # set the parent to the node with the smallest G in the open list
        # print("Parent x and y: ", par.x, ", ", par.y)
        if par.equals(end): # if the parent is the end node, end
            print(par.G)
            print_path(par, map)
            break

list_of_maps = []
maps = int(input())
for i in range(maps):
    rows, cols = input().split(" ")
    rows, cols = int(rows), int(cols)
    portals = []
    for j in range(rows):
        k = input()
        portals.append([x for x in k])
    list_of_maps.append(portals)

for map in list_of_maps:
    find_path(map)

"""
Add start to open
while (open is not empty)
    add non-closed valid neighbors of par to open list, calculate G for each
        set parent of each neighbor to par
        if neighbor already in open list, update g and parent if current g < prev g
    select node with min g, make it new par
    remove par from open list and add to closed list
    check if par == end
"""




