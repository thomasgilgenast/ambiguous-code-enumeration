class Node(object):
    def __init__(self, sequence, max_value=25):
        self.sequence = tuple(int(e) for e in sequence)
        self.max_value = max_value
        self.parents = []
        self.children = []

    def merge(self, indices):
        new_sequence = list(self.sequence)
        merged_string = ''.join([str(self.sequence[i]) for i in indices])
        # skip merges that just stick a leading zero onto an existing number
        # they are equivalent to dropping an 'a' from the word
        if merged_string.startswith('0'):
            return
        merged_value = int(merged_string)
        for index in sorted(indices, reverse=True):
            new_sequence.pop(index)
        # disallow illegal decodings (new element beyond max_value)
        if merged_value <= self.max_value:
            new_sequence.insert(indices[0], merged_value)
            return Node(new_sequence, max_value=self.max_value)

    def get_children(self):
        children = []
        for i in range(len(self.sequence) - 1):
            child = self.merge([i, i+1])
            if child:
                children.append(child)
        return children

    def __str__(self):
        if self.max_value <= 25:
            string = ''.join([chr(97 + e) for e in self.sequence])
            return '%s = %s' % (self.sequence, string)
        return str(self.sequence)

    def __repr__(self):
        return str(self)
