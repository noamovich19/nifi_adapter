class TreeNode(object):
    def __init__(self, value=None):
        self.value = value
        self.children = []

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return str(self.value)

    def add_children(self, children):
        if children is not list:
            children = [children]
        self.children += children

    def remove_children(self, tree_node):
        self.children = [child for child in self.children if child != tree_node]

    def copy(self):
        new_tree = TreeNode(self.value)
        for child in self.children:
            new_tree_child = child.copy()
            new_tree.add_children(new_tree_child)
        return new_tree

    @property
    def leafs(self):
        def scan(tree, leafs):
            if tree.children:
                for child in tree.children:
                    scan(child, leafs)
            else:
                leafs.append(tree)

        tree_leafs = []
        scan(self, tree_leafs)
        return tree_leafs

    def add_to_leafs(self, trees_to_add):
        trees_to_add = trees_to_add if type(trees_to_add) is list else [trees_to_add]
        for leaf in self.leafs:
            leaf.children = trees_to_add

    def repr(self):
        def p_repr(tree, depth):
            print "****" * depth + str(tree.value)

            if type(tree.children) is not list:
                print ""
            for child in tree.children:
                p_repr(child, depth + 1)

        p_repr(self, 0)


def get_processor_tree(processor):
    def set_tree(processor, tree):
        for sibling in processor.siblings:
            new_tree = TreeNode(sibling)
            tree.add_children(new_tree)
            set_tree(sibling, new_tree)

    processor_tree = TreeNode(processor)
    set_tree(processor, processor_tree)
    return processor_tree


def get_group_tree(processor_group):
    processor_group_tree = TreeNode(processor_group)
    for start_processor in processor_group.start_processors:
        start_processor_tree = get_processor_tree(start_processor)
        processor_group_tree.add_children(start_processor_tree)
    return processor_group_tree


def open_group_inside_tree(group_tree_node_parent, group_tree_node):
    group_tree_node_parent.remove_children(group_tree_node)
    open_group_tree_node = get_group_tree(group_tree_node.value)
    for start_processor_tree in open_group_tree_node.children:
        leafs = start_processor_tree.leafs
        for group_child_tree in group_tree_node.children:
            for leaf in leafs:
                leaf.add_children(group_child_tree)
        group_tree_node_parent.add_children(start_processor_tree)


def open_groups(tree):
    def open_groups_one_layer(tree):
        number_of_open_groups = 0
        for child in tree.children:
            if child.value.is_group:
                open_group_inside_tree(tree, child)
                number_of_open_groups += 1
            open_groups_one_layer(child)
        return number_of_open_groups

    while True:
        number_of_open_groups = open_groups_one_layer(tree)
        if number_of_open_groups == 0:
            break
