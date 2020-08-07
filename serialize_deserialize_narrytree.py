class Node:
    def __init__(self, val):
        self.val = val 
        self.children = []

class Codec:
    def serialize(self, root):
        if root is None:
            return ""
        res = [root.val, "#"]
        q = collections.deque([root])
        while q:
            node = q.popleft()
            for child in node.children:
                res.append(child.val)
                q.append(child)
            res.append("#")
        return ",".join(res)

    def deserialize(self, s):
        if len(s) == 0:
            return
        vals = s.split(",")
        q = collections.deque()
        root = Node(vals[0])
        q.append(root)
        i = 1
        while q:
            node = q.popleft()
            i += 1
            while vals[i] != "#":
                child = Node(vals[i])
                node.children.append(child)
                q.append(child)
                i += 1
        return root
