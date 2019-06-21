import sys
sys.path.insert(0, '../graph')
from util import Stack


class Node:
    def __init__(self, v):
        self.value = v
        self.parents = []
        self.children = []

    # def __hash__(self):
    #     return self.v

    # def __eq__(self, other):
    #     return other.value == self.value

    def child_link(self, node):
        self.children.append(node)

    def parent_link(self, node):
        self.parents.append(node)


created = set()


class Tree:
    def __init__(self, links):
        for p, c in links:
            p_node = self.get_node(p)
            c_node = self.get_node(c)
            self.link(p_node, c_node)

    def __str__(self):
        res = ''
        for node in created:
            res += f'node: {node.value}:'
            children = [str(child.value) for child in node.children]
            res += '  children: [' + ' '.join(children) + ']'
            parents = [str(parent.value) for parent in node.parents]
            res += '  parents: [' + ' '.join(parents) + ']\n'
        return res

    def find_node(self, value):
        for node in created:
            if node.value == value:
                return node
        return None

    def get_node(self, value):
        node = self.find_node(value)
        if node is None:
            node = Node(value)
            created.add(node)
            return node
        return node

    def link(self, p_node, c_node):
        p_node.child_link(c_node)
        c_node.parent_link(p_node)

    def dfs(self, starting_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """

        def get_path(p):
            res = ''
            res = ' '.join(
                [str(e.value) if e is not None else '-1' for e in path])
            return res

        # Destination vertex is always None.
        # We want to keep going up until there are no parents.
        destination_vertex = None

        # Create an empty set to store visited nodes
        visited = set()

        # Create an empty Queue and enqueue A PATH TO the starting vertex
        s = Stack()
        s.push([self.find_node(starting_vertex)])

        # A list to hold all paths to the parent nodes
        paths = []

        # While the queue is not empty...
        while s.size() > 0:
            # Dequeue the first PATH
            path = s.pop()

            # GRAB THE VERTEX FROM THE END OF THE PATH
            v = path[-1]

            # IF VERTEX = TARGET, RETURN PATH
            if v == destination_vertex:
                paths.append(path.copy())
                s.pop()  # Remove the None type path
                continue  # Continue processing other paths

            # If that vertex has not been visited...
            if v not in visited:
                # Mark it as visited
                visited.add(v)
                # Then add A PATH TO all of its neighbors to the back
                # of the queue
                if len(v.parents) == 0:
                    p = path.copy()
                    p.append(None)
                    s.push(p)
                else:
                    for neighbor in v.parents:
                        # Copy the path
                        p = path.copy()
                        # Append neighbor to the back of the copy
                        p.append(neighbor)
                        # Enqueue copy
                        s.push(p)

        max_len = 0
        earliest_ancestor = None
        if (len(paths) == 0) or ((len(paths) == 1) and (len(paths[0]) == 2) and
                                 (paths[0][0].value == starting_vertex) and
                                 (paths[0][1] is None)):
            return -1

        for path in paths:
            if (len(path) == 2) and (path[0] == starting_vertex) and (path[1]
                                                                      is None):
                continue
            if len(path) > max_len:
                max_len = len(path)
                earliest_ancestor = path[-2]
            elif len(path) == max_len:
                if path[-2].value < earliest_ancestor.value:
                    earliest_ancestor = path[-2]
        return earliest_ancestor.value


def earliest_ancestor(links, element):
    tree = Tree(links)
    return tree.dfs(element)


if __name__ == '__main__':
    test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8),
                      (8, 9), (11, 8), (10, 1)]
    print(f'earliest ancestor:', earliest_ancestor(test_ancestors, 1))
