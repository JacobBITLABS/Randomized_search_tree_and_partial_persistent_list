from LinkedList.field import field

class modification():
    """ Modification Object versioned records in each node"""
    def __init__(self, version: int, field_name: field, value, key: int):
        self.version = version        # version number
        self.field_name = field_name  # field name type
        self.key = key                # key 
        self.value = value            # value/assoc 
