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
    if records:
        ValidateTree(records)
    else:
        return None
    trees = []
    parent = {}
    trees = CreateTree(records)
    parent_hash = {}
    for record in records:
        parent_hash.setdefault(record.parent_id, []).append(record.record_id)
    for parent_id, child_ids in parent_hash.items():
        trees[parent_id].children = [trees[child_id] for child_id in child_ids if child_id != 0]
    tree_array = list(trees.values())
    if len(trees) > 0:
        root = tree_array[0]
    return root

def ValidateTree(records):
    if records[-1].record_id != len(records) - 1:
        raise ValueError('Tree must be continuous')
    if records[0].record_id != 0:
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

def CreateTree(records):
    trees = {}
    for record in records:
        ValidateNode(record)
        trees[record.record_id] = Node(record.record_id)
    return trees
