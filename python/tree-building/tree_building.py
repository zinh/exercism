class Record():
    def __init__(self, record_id, parent_id):
        self.record_id = record_id
        self.parent_id = parent_id


class Node():
    def __init__(self, node_id):
        self.node_id = node_id
        self.children = []


def BuildTree(records):
    root = None
    records.sort(key=lambda x: x.record_id)
    ordered_id = [i.record_id for i in records]
    if records:
        ValidateTree(ordered_id)
    else:
        return None
    trees = []
    parent = {}
    trees = CreateTree(ordered_id, records)
    for record_id in range(len(ordered_id)):
        for node in trees:
            if record_id == node.node_id:
                parent = node
        for record in records:
            if record.parent_id == record_id:
                for node in trees:
                    if node.node_id == 0:
                        continue
                    if record.record_id == node.node_id:
                        child = node
                        parent.children.append(child)
    if len(trees) > 0:
        root = trees[0]
    return root

def ValidateTree(ordered_id):
    if ordered_id[-1] != len(ordered_id) - 1:
        raise ValueError('Tree must be continuous')
    if ordered_id[0] != 0:
        raise ValueError('Tree must start with id 0')

def ValidateNode(node):
    if node.record_id == 0:
        if node.parent_id != 0:
            raise ValueError('Root node cannot have a parent')
    if node.record_id < node.parent_id:
        raise ValueError('Parent id must be lower than child id')
    if node.record_id == node.parent_id:
        if node.record_id != 0:
            raise ValueError('Tree is a cycle')

def CreateTree(ordered_id, records):
    trees = []
    for record_id in range(len(ordered_id)):
        for record in records:
            if ordered_id[record_id] == record.record_id:
                ValidateNode(record)
                trees.append(Node(ordered_id[record_id]))
    return trees
