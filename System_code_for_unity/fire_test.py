from system_test4 import *
from system_test4 import map
import pickle
if __name__ == "__main__":
    with open('node.txt', 'rb') as f:
        map.node = pickle.load(f)  # 단 한줄씩 읽어옴
    with open('linked_node_list.txt', 'rb') as f:
        map.linked_node_list = pickle.load(f)  # 단 한줄씩 읽어옴
    print(map.node)
    print(map.linked_node_list)

    fire_test(3, 3, 3, map.node, map.linked_node_list)
    print("fire in 3")
    for i in range(0,map.all_node_num):
        print(i, '->', map.node[i].exit_diret)