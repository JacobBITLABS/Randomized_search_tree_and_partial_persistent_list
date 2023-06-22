from __future__ import annotations
from LinkedList.field import field
from typing import Tuple
from LinkedList.node import Node
from LinkedList.modification import modification

ANALYSIS = True # determines if the structure counts the number of allocations and the size seperately
if ANALYSIS:
    print("[ANALYSIS MODE]")
    import sys

class LL():
    """ 
    [Partial Linked List] - Node copying 
        - Modify last "live" version 
        - Search in in earlier versions
    """
    # inner class
    class Version:
        """ Version info - Inner class """
        def __init__(self, head: Node = None, size: int = 0):
            """ Constructor """
            self.head = head
            self.size = size

    def __init__(self, allowed_mods = 2):
        """ Linked List Constructor"""
        self.versions = []               # Version: auxiliary structure to access start of versions
        self.version = -1                # we start in version 1s
        self.allowed_mods = allowed_mods
        if ANALYSIS:
            self.space = 0              # space of memory allocations in bytes 
            self.n_space_alloc = 0      # number of allocations

    def head_in(self, version):
        """ Return the head of given version """
        return self.versions[version].head

    def head(self):
        """ Return the head of the newest version """
        return self.versions[-1].head

    def search(self, version, index) -> Tuple[int, int]:
        """ Access element at a given index in a given version """
        # get head in version
        node: Node = self.head_in(version)
        # print("found head in version: ", version, "head: ", node, "head.key", node.key)
        # iterate to index in version
        for _ in range(index):
            node = node.next_in(version)

        return (node.key_in(version), node.data_in(version))

    def insert(self, index, key: int, k_mark: int = None):
        new_version: self.Version = self.Version()
        # update version here to match in update_field()
        self.version += 1
        # new node
        new_node = Node(key=key, allowed_mods=self.allowed_mods) # persistent node
        # print("new_node allocated address: ", new_node)
        if ANALYSIS:
            self.space += sys.getsizeof(Node) # add size in bytes
            self.n_space_alloc += 1 

        if(k_mark):
            print("Inserting assoc Node()...")
            # insert node on assoc
            new_node.assoc = Node(key = k_mark, allowed_mods=self.allowed_mods)

            if ANALYSIS:
                self.space += sys.getsizeof(Node) # add size in bytes
                self.n_space_alloc += 1 

        if(len(self.versions) > 0 and self.head()):
            new_head: Node = self.head()
            # go trough list until position is found or index > size
            current_head: Node = self.head()
            to_be_next: Node = current_head     # init to first element in list -> head
            to_be_prev: Node = None
            last_node: bool = False             # flag for insertion in end of list
            last_seen_empheral: Node = None     # last previous node

            # print("current_head: ", current_head)
            # print("insertion index: ", index)

            for _ in range(0, index):
                # print("At node: ", i)
                # print("node.key: ", to_be_next.key)

                # Save pointer to last empheral node with non-None assoc field
                if(to_be_next.assoc is not None):
                    # assoc field is containing something. Save pointer to assoc Nodes
                    last_seen_empheral = to_be_next
                    # print("last_seen_empheral: ",last_seen_empheral, " data: ", last_seen_empheral.assoc.key())

                if(to_be_next.next()):
                    #print("going to to_be_next.next()", to_be_next.next().key, "\n")
                    to_be_next = to_be_next.next()
                else:
                    #print("NO NEXT")
                    to_be_prev = to_be_next
                    to_be_next = None   # effectively last element
                    last_node = True    # our node is the last one - no need to search for assoc node
                    break

            """
            from above we know if our node is the last one -> if else clause is activate then we are last
            """
            if (k_mark and not last_node): # assoc field automatically set to None.
                assoc_ptr = None
                # locate the next node in list. Traverse the nodes after to see is they have a non-None assoc field in this version
                if to_be_prev is not None and to_be_prev.next():
                    # there is a node after
                    node = to_be_prev.next() # this position we essentially are cutting in between.
                    while node is not None:
                        # still a node to look in!
                        if(node.assoc):
                            # ptr to node with val in.
                            assoc_ptr = node.assoc 
                            break # stop when first one is found
                        else:
                            # go to next node or None
                            node = node.next() 
            
                # assign assoc_ptr to new node
                new_node = self.update_field(new_node, field.DATA, assoc_ptr, new_head)
                
    
            if(last_seen_empheral and k_mark):
                # connected last seen emerald node with newly inserted
                # print("[last_seen_empheral]: ",last_seen_empheral , "KEY: ",last_seen_empheral.assoc.key())
                last_seen_empheral.assoc = self.update_field(last_seen_empheral.assoc, field.NEXT, new_node.assoc, last_seen_empheral.assoc)

            # if we inserted at effectively on index 0, push new head on heads list
            if(to_be_next == current_head):
                print("to_be_next == current_head")
                new_version.head = new_node
            else:
                # version is the 'same'
                print("The head is the same in the new version")
                new_version.head = current_head

            if(to_be_prev):  # not first node that we insert
                to_be_prev_is_head: bool = to_be_prev == current_head
                # set next field mod in to_be_prev, hence to_be_prev.next is not set directly here
                to_be_prev = self.update_field(to_be_prev, field.NEXT, new_node, new_head)
                new_node.next_back_ptr = to_be_prev

                if(to_be_prev_is_head):
                    new_version.head = to_be_prev
                else:
                    if(new_version.head is not new_head):
                        new_version.head = new_head

            new_version.size = 1 + self.versions[-1].size  # last element.size
            # print("Appending new version of size: ", new_version.size)
    
            # if (new_version.head == new_node):
            self.versions.append(new_version)

        else:
            # just insert new head
            # print("Inserting new head...")
            new_version.head = new_node
            new_version.size = 1
            self.versions.append(new_version)

        print("inserted value: ", key, " at index ",
              index, " in version: ", self.version)

    def update_field(self, node: Node, field_name: field, value: Node, head: Node) -> Node:
        """setting next field """
        if(node.n_mods < self.allowed_mods):
            # not exceeded hyper-parameter limit
            # print("below MAX_MODS")
            mod = modification(version=self.version, field_name=field_name, value=value, key=node._key) # insert next ptr pointing at value
            node.mods[node.n_mods] = mod    # insert the modification on next index
            node.n_mods += 1                # increment the number

        else:
            # print("above MAX_MODS")

            # create new nodes and copy live node
            copy: Node = Node(key=node.key, allowed_mods=self.allowed_mods)

            if ANALYSIS:
                self.space += sys.getsizeof(Node) # add size in bytes
                self.n_space_alloc += 1 
            
            self.copy_live_node(node, copy, field_name, value, head)
            return copy

        return node

    def copy_live_node(self, node: Node, copy: Node, field_name: field, value: Node, head: Node):
        # copy the latest version of each field (data and forward pointeres) to static field section
        copy.assoc = node.data()
        copy._key = node.key()
        copy.next_ptr = node.next()
        copy.next_back_ptr = node.next_back_ptr

        if field_name == field.DATA:
            copy.assoc = value
        elif field_name == field.KEY:
            copy._key = node.key()
        elif field_name == field.NEXT:
            copy.next_ptr = value
            if(copy.next_ptr):
                copy.next_ptr.next_back_ptr = copy
        else:
            raise ValueError('fieldname not found')

        if(copy.next()):
            copy.next().next_back_ptr = copy

        if(copy.next_back_ptr):
            copy.next_back_ptr = self.update_field(copy.next_back_ptr, field.NEXT, copy, head)
            copy = copy.next_back_ptr.next()

    def update_data(self, node: Node, value: int, val_mark = None):
        """ Set data"""
        # create a new version
        new_version: self.Version = self.Version()
        self.version += 1                           # one more version overall
        new_version.size = self.versions[-1].size   # have the same size as the lastest/newest version
        current_head: Node = self.head()

        # update the data field
        modified_node: Node = self.update_field(node, field.KEY, value, current_head)

        if val_mark:
            node.assoc = self.update_field(node.assoc, field.KEY, val_mark, node.assoc)

        if(modified_node == current_head):
            new_version.head = modified_node
        else:
            new_version.head = current_head 

        self.versions.append(new_version)

    def update(self, index: int, value: int, val_mark = None):
        """ 
        The functions does not return anything as it inserts a mod/record into the node about the new version
        """
        # print("update called with: index: ", index, " value: ", value)
        node: Node = self.head() # get current head

        # iterate list to node
        for _ in range(index):
            node = node.next()

        # Insert mod into node
        self.update_data(node, value, val_mark=val_mark)

    def new_version(self):
        new_version: self.Version = self.Version()
        self.version += 1
        new_version.size = self.versions[-1].size
        current_head: Node = self.head()
        new_version.head = current_head
        self.versions.append(new_version)

    def print_at(self, version: int):
        print("Printing version: ", version)
        head: Node = self.head_in(version)
        n: Node = head
        
        while(n):
            print("node: ", n, n.next_in(version))
            print(n.data_in(version))
            
            n = n.next_in(version)

