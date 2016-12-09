from node import Node


class Tree(object):
    def __init__(self, number_string, max_value=25):
        self.max_value = max_value
        self.root = Node(str(number_string), max_value=self.max_value)
        self.node_table = {self.root.sequence: self.root}

    @classmethod
    def from_letters(cls, letters):
        return Tree(''.join([str(ord(l) - 97) for l in letters.lower()]))

    def explore(self):
        to_explore = [self.root]
        while to_explore:
            parent = to_explore.pop()
            children = parent.get_children()
            for child in children:
                if child.sequence not in self.node_table:
                    self.node_table[child.sequence] = child
                    to_explore.append(child)
                self.node_table[child.sequence].parents.append(parent)
                parent.children.append(self.node_table[child.sequence])

    def __str__(self):
        to_print = list(self.root.children)
        visited = {self.root.sequence}
        lines = []
        while to_print:
            current_node = to_print.pop()
            if current_node.sequence in visited:
                continue
            for parent in current_node.parents:
                lines.append(
                    ('"%s" -> "%s";' % (parent, current_node))
                    .replace('(', '').replace(')', '')
                )
            visited.add(current_node.sequence)
            to_print.extend(current_node.children)
        return '\n'.join(lines)

    def __repr__(self):
        return str(self)
