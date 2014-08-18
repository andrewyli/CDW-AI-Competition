class Box:
    def __init__(self, l, r, u, d):
        # 0 is not filled, 1 is filled by p1, 2 is by p2(l, r, u, d are edges of each box)
        self.left = l
        self.right = r
        self.up = u
        self.down = d
        self.filled = False
