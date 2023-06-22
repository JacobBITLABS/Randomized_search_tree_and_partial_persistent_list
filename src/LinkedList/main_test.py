from ll import LL

"""
This module test the basic functionality of the Partial Linked List
"""

if __name__ == "__main__":
    print("##################################################################")
    print("[Singly Linked List]")
    print("##################################################################")
    
    list = LL()

    print()
    print("[Insert]")
    list.insert(index=0, key=1, k_mark=2)
    print("------------------------------------------------------------------------")
    list.insert(index=1, key=5, k_mark=3)
    print("------------------------------------------------------------------------")
    list.insert(index=2, key=3, k_mark=None)
    print("------------------------------------------------------------------------")
    list.insert(index=3, key=4, k_mark=4)
    print("------------------------------------------------------------------------")

    print()

    # current_head:Node = list.head_in(2)
    # print("current head data", current_head.assoc)

    print("[Testing Heads]")
    h0 = list.head_in(0)
    print("h0.key", h0.key(), ", h0.data.key: ", h0.data())
    print()

    # print("next node")
    # print("h0.next().key(): ", h0.next().key(), ", h0.next().data.key: ", h0.next().data().key())

    print("list size: ", len(list.versions))
    print("[Testing Access]")
    print()
    (n0_key, n0_data) = list.search(version=0, index=0)
    print("n0.key: ", n0_key, " n0_data", n0_data.key())

    print("------------------------------------")
    (n1_key, n1_data) = list.search(version=1, index=1)
    print("n1.key: ", n1_key, " n1_data", n1_data.key())

    print("------------------------------------")
    (n2_key, n2_data) = list.search(version=2,  index=2)
    print("n2.key: ", n2_key, ", n2_data:", n2_data)

    print("------------------------------------")
    (n3_key, n3_data) = list.search(version=3, index=3)
    print("n3.key: ", n3_key, ", n3_data:", n3_data.key())

    print()
    print("[Test Connections in Emerald Nodes - assoc connections]")
    h0 = list.head_in(3)
    eNode = h0.data()
    while(eNode):
        print("eNode key", eNode.key())
        print("------------------------------------")
        eNode = eNode.next()
    print()

    print()
    print("[Test Node Copying]")
    list.update(0,9)
    list.update(0,8)

    (n0_key, n0_data) = list.search(version=0, index=0)
    print("n0.key: ", n0_key, " n0_data", n0_data.key())
    
    # print("* **************************************************** *")
    # print("[Test update]")
    # list.update(index=3, value=2)

    # n4 = list.search(version=4, index=3)
    # print("n4.key", n4)

    # n3 = list.search(version=3,  index=3)
    # print("n3.assoc after modification", n3)

    print()
    print("[Analysis]")
    print("space: ",  list.space, "bytes ", "num allocations: ", list.n_space_alloc, "nodes")