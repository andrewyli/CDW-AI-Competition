class Edge:
    def __init__(self, image, x, y):
        self.image = image
        self.rect = self.image.get_rect().move(x, y)
        self.x = x
        self.y = y
