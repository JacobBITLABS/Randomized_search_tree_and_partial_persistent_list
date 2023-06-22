class RSTNode:
    """Node class for RST"""

    def __init__(self, key, priority):
        self.key = key
        self.left: RSTNode = None
        self.right: RSTNode = None
        self.priority = priority
