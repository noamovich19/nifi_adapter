from processors import processors
from prov_tree import *
import time
import copy

t = get_processor_tree(processors[0])
t.repr()

print "\n-----------\n"
t = t.copy()
t.add_to_leafs([TreeNode(100), TreeNode(40)])
t.repr()


print "\n-----------\n"

t = get_processor_tree(processors[0])
t = t.copy()
t_group = t.children[0]
open_group_inside_tree(t, t_group)
t.repr()

print "\n-----------\n"
time.sleep(1)
t = get_processor_tree(processors[0]).copy()
open_groups(t)
t.repr()