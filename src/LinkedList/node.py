from __future__ import annotations
from LinkedList.field import field
from LinkedList.modification import modification

class Node():
    """
    Node Class
    """
    def __init__(self, key, allowed_mods, assoc=None):
        self.allowed_mods = allowed_mods
        self.n_mods = 0             # init to 0
        self._key = key             # must be set
        self.assoc = assoc          # assoc value can be None
        self.next_ptr = None
        self.next_back_ptr = None
        self.mods = [modification] * self.allowed_mods

    def get_field_at_version(self, field_name: field, v: int) -> Node:
        max_version_i = 0
        in_mods = False  # found in mods

        # print("self.mods: ", self.mods)
        # print("self.n_mods: ", self.n_mods)
        # print("data: ", self.assoc)
        # print("field_name ", field_name)

        for i in range(self.n_mods):                    # for each mods, -1 the one in the dedicated field
            if(self.mods[i].field_name == field_name):  # test field name
                if(self.mods[i].version <= v):          # tests version
                    max_version_i = i
                    in_mods = True  # was found
                else:
                    break

        # if not in mods
        if(not in_mods):
            if field_name ==  field.KEY:
                return self._key
            if field_name == field.DATA:
                return self.assoc
            elif field_name == field.NEXT:
                return self.next_ptr
            else:
                raise ValueError('fieldname not found')

        return self.mods[max_version_i].value  # return

    def get_field(self, field_name: field):
        """Get mod field val: can be both value, next"""
        # return newest mod if there is one

        if(self.n_mods > 0):
            i = self.n_mods
            while(i > 0):
                # print("i", i)
                if(self.mods[i-1].field_name == field_name):
                    return self.mods[i-1].value
                i = i-1

        # if no mod, or no value field:
        if field_name ==  field.KEY:
            return self._key
        if field_name == field.DATA:
            return self.assoc
        elif field_name == field.NEXT:
            return self.next_ptr
        else:
            raise ValueError('fieldname not found')

    def key_in(self, v: int) -> Node:
        return self.get_field_at_version(field.KEY, v)

    def data_in(self, v: int) -> Node:
        return self.get_field_at_version(field.DATA, v)

    def next_in(self, v: int) -> Node:
        # print("in next_in, version: ", v)
        return self.get_field_at_version(field.NEXT, v)

    def key(self):
        return self.get_field(field.KEY)

    def data(self):
        """ Returns ptr to emerald live node"""
        return self.get_field(field.DATA)

    def next(self):
        return self.get_field(field.NEXT)